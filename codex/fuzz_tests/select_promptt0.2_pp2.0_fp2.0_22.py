import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if given, block until at least one file descriptor is ready or the timeout has expired

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sources.

# Example:
# Wait for input on stdin and socket
# import select
# import socket
# import sys
# import Queue

# # Create a TCP/IP socket
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setblocking(0)

# # Bind the socket to the port
# server_address = ('localhost', 10000)
# print >>sys.stder
