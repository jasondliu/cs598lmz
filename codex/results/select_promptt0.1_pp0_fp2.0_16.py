import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sockets, and can be used to implement a simple web server.

# The following example shows how to use select() to handle three clients at once.

import socket
import select

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set socket option
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to a public host, and a well-known port
s.bind(('0.0.0.0', 2
