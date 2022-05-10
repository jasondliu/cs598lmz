import socket
import sys
import math
import time
import os

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = './uds_socket'
print >> sys.stderr, 'connecting to %s' % server_address
