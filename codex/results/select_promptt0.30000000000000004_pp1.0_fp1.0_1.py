import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until a monitored file descriptor becomes ready; if zero, do not block at all; otherwise, block for up to timeout seconds

# select.select(rlist, wlist, xlist[, timeout])
# Return value: three lists of objects that are ready: subsets of the first three arguments.
# When the specified time-out period value, timeout, elapses, three empty lists are returned.

# select.select() can be used as an efficient way to wait until a file descriptor is ready for reading or writing.
# The following example shows how to use select() to wait for a socket to become readable or writable,
# or until a timeout occurs:

import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET
