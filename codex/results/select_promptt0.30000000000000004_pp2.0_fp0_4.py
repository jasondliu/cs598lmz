import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not given, block until a monitored file descriptor becomes ready; if zero, return three empty lists; if a positive number, block at most that number of seconds and return three empty lists if the timeout expires
#
# Return value: three lists of objects that are ready: subsets of the first three arguments
#
# Example:
#
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.bind(('', 0))
# >>> s.listen(1)
# >>> s.getsockname()
# ('0.0.0.0', 54901)
# >>> select.select([s], [], [], 5)
# ([], [], [])
# >>> select.select([s], [], [], 5)
# ([], [], [
