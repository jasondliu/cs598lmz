import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sources.

# Example:
# A simple chat server

import socket
import select

# AF_INET: IPv4
# SOCK_STREAM: TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SO_: socket option
# SOL_SOCKET: socket
# SO_REUSEADDR: the socket can be bound to an address which is already in use
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

