import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until a monitored file descriptor becomes ready; if zero, return immediately even if no file descriptors are ready; if given and not zero, it specifies a timeout in seconds (float) and the function will return three lists after that time if no file descriptors become ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.bind(('localhost', 0))
# >>> s.listen(1)
# >>> select.select([s], [], [])
# ([<socket._socketobject object at 0x7f6f8c0b7d30>], [], [])
# >>> select.select([s], [], [], 0
