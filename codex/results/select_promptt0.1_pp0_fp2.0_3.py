import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until a monitored file descriptor becomes ready; if zero, return immediately even if no file descriptors are ready; if timeout is a float, it specifies a timeout in seconds (float portion is microseconds); otherwise it specifies a timeout in milliseconds

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sources.

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.bind(('', 0))
# >>> s.listen(1)
# >>> s.getsockname()
# ('127.0.0.1', 51596)
# >>> s.setblocking(0)
# >>> s.accept()
# Trace
