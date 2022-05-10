import select
# Test select.select()

# Test select.select()

import socket
import select
import sys
import time

# Some constants
TIMEOUT = 1
HOST = 'localhost'
PORT = 50007

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

# Set the socket to non-blocking mode
sock.setblocking(0)

# The argument to select() is a list of three lists:
#  1) Wait until ready for reading
#  2) Wait until ready for writing
#  3) Wait for errors
timeout = TIMEOUT
readable, writable, exceptional = select.select([sock], [sock], [], timeout)

if not (readable or writable or exceptional):
    print('  timed out, do some other work here')
else:
    print('  w
