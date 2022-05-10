import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not supplied, block until a monitored file descriptor is ready; if supplied as a float, it specifies a timeout in seconds; as an integer, in milliseconds; if zero, do not block at all, but return immediately even if no file descriptors are ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sources in a non-blocking way.

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.connect(('www.python.org', 80))
# >>> s.send(b'GET /index.html HTTP/1.0\r\n\r\n')
# >>> select.select([s], [], [])
#
