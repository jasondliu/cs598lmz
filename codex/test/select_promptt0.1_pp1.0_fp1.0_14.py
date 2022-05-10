import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return immediately even if no file descriptors are ready; if given, it should be a float giving a timeout in seconds (or fractions thereof)

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sockets.

# Example:

# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.bind(('', 0))
# >>> s.listen(1)
# >>> s.getsockname()
# ('127.0.0.1', 54500)
# >>> r, w, x = select.select([s], [], [], 5)
# >>> r

