import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# Example:
# rlist, wlist, xlist = select.select(rlist, wlist, xlist[, timeout])

# If the timeout period expires, three empty lists are returned.

# File descriptor objects may be integers or long integers.

# On Windows, file descriptor objects cannot be used where a file descriptor is expected,
# and also cannot be used as the first argument to select().
# Instead, Windows select() works on sockets, and in this case it can be used with any object that implements the socket interface.

# select.select() is a useful way to multiplex input and output,
# especially when we have multiple sockets to read from.

# The following
