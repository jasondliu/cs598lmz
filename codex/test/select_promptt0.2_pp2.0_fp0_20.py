import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# select.select() returns three lists of objects that are ready: subsets of the first three arguments.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A negative or None timeout means to block indefinitely.

# select.select() will never “miss” a file descriptor becoming ready.
# If a file descriptor becomes ready while it is being monitored by select(),
# the corresponding entry in the returned lists will be accurate when select() returns.

# select.select() can be interrupted by a signal (see the signal module),
# so it should be invoked with care from signal handlers.

# select.select() should not be used if the file descriptors can be in non-blocking mode.
# Use the
