import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input and output.
# It can be used to implement a simple multiplexing server.
# The following example shows a simple echo server that uses select().
# The server handles multiple clients at a time using select().
# The server handles one connection at a time,
# but it could easily be modified to handle multiple connections simultaneously.

import socket
import select

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
server.bind(server_
