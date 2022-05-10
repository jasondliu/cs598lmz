import select
# Test select.select()

# select.select() takes three lists of file descriptors and waits until
# some of them are ready for some kind of I/O.
# The first list is the list of file descriptors to be checked for being
# ready to read.
# The second list is the list of file descriptors to be checked for being
# ready to write.
# The third list is the list of file descriptors to be checked for error
# conditions.
# The return value is a triple of lists of file descriptors: the subset of
# the first three parameters that are ready for the corresponding I/O
# operations.

# The following example shows how to use select() to monitor a pair of
# sockets and stdin for input.

import socket
import sys

# Create two sockets.
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the first socket to localhost:8000.
s1.connect(('localhost', 8000))

# Connect the second socket to
