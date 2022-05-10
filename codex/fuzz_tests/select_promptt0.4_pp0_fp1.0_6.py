import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not given, block until a file descriptor is ready; if zero, return immediately even if no file descriptors are ready; otherwise, block for the given number of seconds

# Returns three lists of file descriptors: those that are ready for reading, those that are ready for writing, and those that have an exceptional condition pending.
# If the time limit is exceeded, three empty lists are returned.

# select.select() is a useful way to multiplex input and output over a set of file descriptors.
# It can be used to implement a simple multiplexing loop.
# The following example illustrates how to use select.select() to monitor a set of sockets and file descriptors for readable data.

import socket
import select
import Queue

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET,
