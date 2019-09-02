#!/usr/bin/python3
#
import socket
import sys
import argparse
import yaml

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True, help="config file")

args = parser.parse_args()
with open(args.file) as stream:
    data = yaml.safe_load(stream)

host = data['host']
port = data['port']
node_number = data['node_number']

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
myhostname = socket.gethostname()
try:
    sock.bind(server_address)
    sock.listen(1)
    while True:
        print('waiting for a connection', file=sys.stderr)
        connection, client_address = sock.accept()
        print('connection from {}'.format(client_address), file=sys.stderr)
        connection.sendall(('Connected on node [nodenumber: {}, hostname: {}]\r\n'.format(node_number, myhostname)).encode())
        connection.close()
finally:
    sock.close()
