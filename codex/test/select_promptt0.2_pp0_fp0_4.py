import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# If the time out is omitted the function blocks until at least one file descriptor is ready.
# A time out value of zero specifies a poll and never blocks.

# If the time out is negative the function blocks indefinitely.

# select.select() is a useful way to multiplex input from multiple sockets.

# Example:

# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.bind(('', 0))
# >>> s.listen(1)
# >>> s.getsockname()
# ('0.0.0.0', 51898)
# >>> r, w, x = select.select([s], [], [], 5)
# >>> r
# [<socket._socketobject object
