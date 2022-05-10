import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until a monitored file descriptor becomes ready; if zero, return immediately even if no file descriptors are ready; otherwise, block for at most timeout seconds

# Return value: three lists of objects that are ready: subsets of the first three arguments

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.bind(('localhost', 8888))
# >>> s.listen(1)
# >>> s.accept()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python2.7/socket.py", line 202, in accept
#     sock, addr = self._sock.accept()
# error: [Errno 11
