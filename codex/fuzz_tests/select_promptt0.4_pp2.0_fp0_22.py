import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: a time-out as a floating point number in seconds (or None for no time-out)
# Return value: three lists of objects that are ready: subsets of the first three arguments
# If the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

# The select() function supports a timeout. If the timeout is 0.0, then select() will return immediately.
# If the timeout is None, then select() will block until a monitored file descriptor becomes ready.
# Otherwise, the timeout argument specifies a time-out as a floating point number expressed in seconds.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A negative or None timeout means an infinite wait.
#
# The select() function can monitor sockets, open files, and pipes.
# The return
