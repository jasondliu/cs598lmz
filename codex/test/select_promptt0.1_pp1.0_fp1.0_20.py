import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sockets, but it has some limitations.
# It can only monitor sockets, not arbitrary file descriptors.
# It can only monitor sockets for a single thread.
# It can only monitor sockets for reading, writing, or an exceptional condition.
# It cannot monitor sockets for accept() or connect() operations.
# It cannot monitor sockets for timeouts.

# select.select() is a useful way to multiplex input from multiple sockets, but it has some limitations.
# It can only monitor sockets, not arbitrary file descriptors.
# It can only monitor sockets for a single thread.
# It can only monitor
