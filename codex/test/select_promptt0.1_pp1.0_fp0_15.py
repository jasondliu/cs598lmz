import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output, especially when there are multiple sockets to be monitored.

# Example:

# import select
# import socket
# import sys

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.setblocking(0)

# server_address = ('localhost', 10000)
# print >>sys.stderr, 'starting up on %s port %s' % server_address
# server.bind(server_address)

# server.listen(5)

# inputs = [ server ]
# outputs = [
