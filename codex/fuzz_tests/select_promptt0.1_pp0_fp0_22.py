import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if given, block for at least that many seconds (can be a float)

# Return value: three lists of objects that are ready: subsets of the first three arguments

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.bind(('localhost', 50000))
# >>> s.listen(1)
# >>> select.select([s], [], [])
# ([<socket._socketobject object at 0x7f7c9d8b8d10>], [], [])
# >>> select.select([s], [], [], 5.0)
# ([], [], [])
# >>> select.select([s],
