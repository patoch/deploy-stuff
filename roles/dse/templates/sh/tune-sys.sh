#!/usr/bin/env bash
echo deadline > /sys/block/vda/queue/scheduler
echo 0 > /proc/sys/vm/zone_reclaim_mode

# readadhead to 64 
blockdev --setra 64 /dev/vda1

# swap off
echo  1 > /proc/sys/vm/swappiness
swapoff --all


# user limits
grep -q -F '* - nproc 32768' /etc/security/limits.d/90-nproc.conf || echo '* - nproc 32768' >> /etc/security/limits.d/90-nproc.conf
grep -q -F 'vm.max_map_count = 131072' /etc/sysctl.conf || echo 'vm.max_map_count = 131072' >> /etc/sysctl.conf