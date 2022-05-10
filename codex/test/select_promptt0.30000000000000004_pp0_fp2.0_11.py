import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.error: exception raised in case of an error

# select.select() can be interrupted by a signal (see the signal module)

# select.select() supports three file descriptor lists:
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# The return value is a tuple of three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready.
# When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

# A file descriptor is considered ready if it is possible to perform the corresponding I/O operation (e
