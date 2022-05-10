import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments
# If the time limit is exceeded, three empty lists are returned

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.bind(('localhost', 50000))
# >>> s.listen(1)
# >>> s.setblocking(0)
# >>> select.select([s], [], [], 5)
# ([<socket._socketobject object at 0x7f2d6c2c6d00>], [], [])
# >>> select.select([s], [], [], 5)
# ([], [], [])
# >>> select.select([s], [
