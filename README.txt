CasOps enables you to deploy automatically a multi-dc Casandra cluster, with agents and OPSCenter.

OS supported:
Centos 6.6

Cassandra supported:
DSC 2.1.9

Snitch:
GossipingPropertyFileSnitch only.

Steps :
- Startup the machines with OS
- Register the machine in the DNS or in /etc/hosts so that hostname and fqdn are properly set.
- Edit /hosts:
---- under [cassandra-all:vars], set seeds and opsc_ip
---- under [opscenter] set OPSCenter ip
---- under each [cassandra-dcXXX-racYYY] add the ips of nodes belonging to the dc and rack (modify the file to add more DCs or RACs)
---- optionnaly : change DC and rack names in [cassandra-dcXXX-racYYY:vars]
- Change cassandra configuration files in /roles/dsc-cassandra/templates/conf to what you like. 
- IMPORTANT: Check and change (it may not run on your machine, as disk setup changes, so test it) the os tuning script to whatever best fits to your hardware: /roles/dsc-cassandra/templates/sh/tune-sys.sh
- install Cassandra and agents: ansible-playbook -i hosts install-cas.yaml
- install OPSCenter: ansible-playbook -i hosts install-opsc.yaml


