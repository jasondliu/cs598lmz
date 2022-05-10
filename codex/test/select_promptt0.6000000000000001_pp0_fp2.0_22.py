import select
# Test select.select()

# Create a pair of connected sockets

# Create a pair of connected sockets

import socket
import sys
import time
import os

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create server socket that will listen for a connection request
# Sock1 will be the server

server_address_1 = ('localhost', 10000)
server_address_2 = ('localhost', 10001)
print('starting up on {} port {}'.format(*server_address_1))
print('starting up on {} port {}'.format(*server_address_2))
sock1.bind(server_address_1)
sock2.bind(server_address_2)

# Listen for incoming connections
sock1.listen(1)
sock2.listen(1)

conn1, client_address1 = sock1.accept()
conn2, client_address2 = sock2.accept()
