import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input/output over a number of sockets or other file-like objects.
# It can also be used to wait for a file descriptor to become ready for some class of I/O operation (e.g., input possible).
# The following example shows how to multiplex input from two sockets and standard input:

# import select
# import socket
# import sys
# import Queue

# # Create a TCP/IP socket
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setblocking(0)

# # Bind the socket to the port
# server_address = ('
