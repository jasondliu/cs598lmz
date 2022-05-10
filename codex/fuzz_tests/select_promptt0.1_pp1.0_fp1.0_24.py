import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if given, block for at least that many seconds (can be a float)

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sockets.

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.connect(('www.python.org', 80))
# >>> s.send(b'GET /index.html HTTP/1.0\r\n\r\n')
# >>> select.select([s], [], [])
# ([<socket.socket fd=3, family=AddressFamily.AF_INET, type
