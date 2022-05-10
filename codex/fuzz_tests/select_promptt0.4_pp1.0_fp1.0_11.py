import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, wait forever

# select.select() returns three lists of objects that are ready: subsets of the first three arguments. When the timeout argument is omitted the function blocks until at least one file descriptor is ready. A zero timeout causes the function to return immediately, even if no file descriptors are ready; this can be used to poll().

# select.select() can be interrupted by a signal (see the signal module); the exception raised will be select.error, and the errno attribute is set to EINTR.

# The select() function is a part of the POSIX standard, and is available on Unix and Unix-like systems.

# On Windows, only sockets are supported; on Unix, all file descriptors can be used.

# The select() function is also available as a part of the fcntl module.
