import socket
import threading
import json
import time

import argparse

from utils import *

parser = argparse.ArgumentParser()
parser.add_argument('--host', help="host's ip address", default='localhost')
parser.add_argument('--port', type=int, help="host's port", default=9000)
parser.add_argument('--id', type=int, help="client id", required=True)

args = parser.parse_args()

ID = args.id
PORT = args.port
HOST = args.host

# Create a TCP/IP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)

# Connect the socket to the port where the server is listening
socket.connect(server_address)
print("Connected to", server_address)

# Send id
socket.sendall(bytes(str(ID)+'\n', "utf-8"))

# Receive message from host
data = socket.recv(1024)
print
