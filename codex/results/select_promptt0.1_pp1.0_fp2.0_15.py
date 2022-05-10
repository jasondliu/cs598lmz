import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input/output over a number of sockets or other file-like objects.

# Example:
# import select
# import socket
# import sys
# import Queue

# # Create a TCP/IP socket
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setblocking(0)

# # Bind the socket to the port
# server_address = ('localhost', 10000)
# print >>sys.stderr, 'starting up on %s port %s' % server_address
# server.bind(server_address)

# # Listen for incoming connections
