import select
# Test select.select in python
# https://docs.python.org/2/library/select.html

import sys, time
from socket import *

timeout = 5
host = 'localhost'
port = 50008

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((host, port))

print "READ & WRITE return a list of sockets ready for reading or writing."
print "Select call: read: ", sock.fileno(), " error: ", sock.fileno()
r, w, e = select.select([sock], [sock], [sock], timeout)
print "Select return: read: ", r, " write: ", w, " error: ", e

print "Rread return only a list of sockets ready for reading."
print "Select call: read: ", sock.fileno()
r, w, e = select.select([sock], [], [], timeout)
print "Select return: read: ", r, " write: ", w, " error: ", e

print "Write return only a list of sockets ready for writing."
print "Select call: write
