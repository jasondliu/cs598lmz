import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value is a tuple of three lists of objects that are ready: subsets of the first three arguments.
# When the time-out is reached without a file descriptor being ready, three empty lists are returned.
# If a file descriptor is ready, it is included in the appropriate subset.

# select.select() is a blocking call.
# select.select() can also handle non-socket objects.
# select.select() can also be interrupted by a signal (this is usually only possible in the main thread).
# select.select() supports an additional fourth argument: a timeout.
# If the timeout is omitted, select() can block indefinitely.
# If the timeout is zero, select() will return immediately, without waiting for any file descriptors to become ready.
# If the timeout is a positive number, it specifies the maximum number of seconds that select()
