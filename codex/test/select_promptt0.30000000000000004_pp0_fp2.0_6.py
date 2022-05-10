import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments
# If the timeout is reached without a file descriptor becoming ready, three empty lists are returned.

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.bind(('localhost', 50000))
# >>> s.listen(1)
# >>> select.select([s], [], [])
# ([<socket._socketobject object at 0x7f1d6a0c4d90>], [], [])
# >>> select.select([s], [], [], 3)
# ([], [], [])
# >>> select.select([s], [], [], 5)
#
