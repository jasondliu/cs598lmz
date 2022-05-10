import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified or None, block until at least one file descriptor is ready; otherwise, block for at least that many seconds

# Returns three lists of file descriptors: subsets of the first three arguments
# The first list contains those descriptors that are ready for reading, the second contains those that are ready for writing, and the third those that have an exceptional condition pending.

# The select() call is a way to ask the kernel “who’s ready for I/O?”
# The kernel maintains a set of file descriptors that are ready for I/O.
# The select() call asks the kernel to update the sets of file descriptors that are ready, and to return the current values.

# The select() call is a way to ask the kernel “who’s ready for I/O?”
