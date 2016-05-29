STEPS = 100
KEYSPACE = "manager"
TABLE = "manager_config"
DC = ""

### ----------------------
RANGE_MIN = -(2**63)
RANGE_MAX = (2**63)-1
TOKEN_COUNT = (RANGE_MAX - RANGE_MIN)
TOKEN_COUNT_BY_STEP = TOKEN_COUNT / STEPS

if not DC == "":
	DC = "-dc %d " % DC

current_min = RANGE_MIN
current_max = current_min + TOKEN_COUNT_BY_STEP

print "nodetool repair %s -par -st %s -et %s %s %s" % (DC, current_min, current_max, KEYSPACE, TABLE)

while True:
	current_min = current_max
	current_max = current_min + TOKEN_COUNT_BY_STEP
	if current_min > 0 and current_min < 10:
		current_min = 10
	if current_min < 0 and current_min > -10:	
		current_min = -10
	if current_max > 0 and current_max < 10:	
		current_max = 10
	if current_max < 0 and current_max > -10:	
		current_max = -10		

	if current_max > RANGE_MAX:
		print "nodetool repair %s-par  -st %s -et %s %s %s" % (DC, current_min, RANGE_MAX, KEYSPACE, TABLE)
		exit(0)
	print "nodetool repair %s-par -st %s -et %s %s %s" % (DC, current_min, current_max, KEYSPACE, TABLE)


