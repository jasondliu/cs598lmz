import socket
import sys
import time
import pickle
import random
import os
import math

# Global variables

# Global variables
server_address = ('localhost', 10000)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

# Send data
message = 'This is the message.  It will be repeated.'
print('sending {!r}'.format(message))
sock.sendall(message.encode())

# Look for the response
amount_received = 0
amount_expected = len(message)

while amount_received < amount_expected:
    data = sock.recv(16)
    amount_received += len(data)
    print('received {!r}'.format(data))

# Send data
message = 'This is the message.  It will be repeated.'
print('sending {!r}'.
