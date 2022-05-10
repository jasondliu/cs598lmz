import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.bind(('localhost', 50000))
# >>> s.listen(1)
# >>> s.accept()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python2.7/socket.py", line 202, in accept
#     sock, addr = self._sock.accept()
# socket.error: [Errno 11] Resource temporarily unavailable
# >>> select.select([s], [], [])
# ([<socket._socketobject object at 0
