# CASOPS
CasOps enables you to deploy automatically a multi-dc Casandra cluster, with agents and OPSCenter.

###Requirements
- Centos 6.6
- DSC 2.1.9
- Snitch: GossipingPropertyFileSnitch only.

### Setup :
* Install and start the machines 
* Register the machine in the DNS or in /etc/hosts with hostname and properly set fqdn.
* Edit /hosts:
    * under [cassandra-all:vars], set seeds and opsc_ip
    * under [opscenter] set OPSCenter ip
    * under each [cassandra-dcXXX-racYYY] add the ips of nodes belonging to the dc and rack (modify the file to add more DCs or RACs)
    * optionnaly : change DC and rack names in [cassandra-dcXXX-racYYY:vars]
* Change cassandra configuration files in /roles/dsc-cassandra/templates/conf to what you like. 
* Tune system (it may require changes for you) /roles/dsc-cassandra/templates/sh/tune-sys.sh
* Install Cassandra and agents: ansible-playbook -i hosts install-cas.yaml
* Install OPSCenter: ansible-playbook -i hosts install-opsc.yaml


