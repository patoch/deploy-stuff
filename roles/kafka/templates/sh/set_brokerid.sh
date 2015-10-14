#!/usr/bin/env bash

ip="$(ip a s eth0 | awk '/inet / {print$2}' | cut -d/ -f1)"
broker_id="$(ip a s eth0 | awk '/inet / {print$2}' | cut -d/ -f1 | sed 's/\.//g')"

sed -i.bak "s/^\(broker.id=\).*/\1$broker_id/" /opt/kafka/config/server.properties

sed -i "s/host.name=localhost/host.name=$ip/g" /opt/kafka/config/server.properties