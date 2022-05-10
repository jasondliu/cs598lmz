import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select() can be used to monitor multiple file descriptors, waiting until one or more of the file descriptors become “ready” for some class of I/O operation (e.g., input possible).

# The first three arguments are sequences of file descriptors to be waited for: rlist, wlist, xlist — which can be modified on return (since they are passed by reference).

# The optional fourth argument specifies a timeout in seconds; it may be a floating point number to specify fractions of seconds. If it is absent or None, the call will never time out.

# The return value is a tuple of three lists corresponding to the first three arguments; each contains the subset of the corresponding file descript
