import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output, especially when there are multiple sockets to be monitored.

# Example:
# This example shows how to use select() to monitor two sockets at the same time.

import socket
import select

# create a pair of connected sockets
sock1, sock2 = socket.socketpair()

# make sock2 non-blocking
sock2.setblocking(0)

# create a pair of connected sockets
sock1, sock2 = socket.socketpair()

# make sock2 non-blocking
sock2.setblocking(0)

# make sock1 non-
