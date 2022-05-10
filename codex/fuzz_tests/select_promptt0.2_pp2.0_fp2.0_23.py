import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# The select() function monitors all of the file descriptors listed in its first three arguments until they become “ready” for some class of I/O operation (e.g. input possible).
# The first three arguments are sequences of file descriptors to be monitored.
# The first three lists passed to select() are modified in place to indicate which descriptors are ready.
# The return value is a tuple of three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# When the timeout argument is present and not None, it should be a floating point number specifying a timeout
