import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Returns three lists of objects that are ready: subsets of the first three arguments.

# Example:

# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.connect(('www.python.org', 80))
# >>> s.send(b'GET / HTTP/1.0\r\n\r\n')
# >>> select.select([s], [], [], 1.0)
# ([<socket._socketobject at 0x7f9b8e8c8f70>], [], [])
# >>> s.recv(1000)
# b'HTTP/1.1 301 Moved Permanently\r\n'
# >>>

# select.select()
