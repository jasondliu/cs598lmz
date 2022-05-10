import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor is ready

# Return value: three lists of objects that are ready

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.bind(('localhost', 8080))
# >>> s.listen(5)
# >>> s.setblocking(0)
# >>> select.select([s], [], [], 5)
# ([<socket._socketobject object at 0x7f5c5a9b9d90>], [], [])
# >>> select.select([s], [], [], 5)
# ([], [], [])
# >>> select.select([s], [], [], 5)
# ([], [], [])
# >>> select.select([s],
