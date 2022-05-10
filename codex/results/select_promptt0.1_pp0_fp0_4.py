import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.connect(('www.python.org', 80))
# >>> s.send(b'GET / HTTP/1.0\r\n\r\n')
# >>> select.select([s], [], [], 1.0)
# ([<socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52333), raddr=('151.101.0.223', 80
