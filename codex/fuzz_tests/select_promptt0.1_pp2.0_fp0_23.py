import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output,
# allowing your program to monitor many file descriptors at once and respond immediately to whichever ones need attention.

# select.select() is also useful for implementing timeouts.
# If you pass a non-negative timeout value, it will block at most that many seconds and
# may return sooner if a file descriptor becomes ready.
# The actual timeout value will be an integer multiple of the underlying timer resolution,
# and may be longer than requested.

# select.select() can also be interrupted by a signal (such as SIGALRM),
# so if you get a signal, you should call select
