#!/bin/bash
apt-get update
apt-get install -y python3 python3-yaml
python3 /demo-apps-for-docker/simple-tcp-server/server.py --file /demo-apps-for-docker/simple-tcp-server/server-config.yml

