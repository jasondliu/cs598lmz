import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select() uses a timeout value of zero, so it will return immediately if none of the file descriptors are ready.

# select() is available on Unix and Windows.

# select() supports file descriptors on Unix, and Windows sockets on Windows.

# select() can be interrupted by a signal (such as SIGINT or SIGALRM) if the system supports restarting select() after the signal handler returns.

# select() can also be interrupted by a signal on some systems, and on some systems it is not restartable in that case.

# select() can indicate that a file descriptor is “ready” based on conditions other than input or output being available.
