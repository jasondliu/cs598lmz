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

# select.select() can be interrupted by a signal (see the signal module) and in such cases returns three empty lists.
# select.select() is intended for waiting until a file descriptor is ready for I/O;
# it can’t be used to wait until a file descriptor becomes “ready” for some other condition,
# such as until a file descriptor is closed.

# select.select() can be used to monitor multiple file descriptors, waiting until one or more of the file descriptors
