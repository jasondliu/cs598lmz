import select
# Test select.select()

# select.select()
# select.select(rlist, wlist, xlist[, timeout])

# select.select() monitors the file descriptors in the lists rlist, wlist, and xlist,
# waiting until one or more of the file descriptors become "ready" for some class of I/O operation
# (e.g. input possible, output possible, an exceptional condition)

# The first three arguments are sequences of file descriptors to be waited for:
# rlist -- wait until ready for reading
# wlist -- wait until ready for writing
# xlist -- wait for an "exceptional condition" (see the manual page for what your system considers such a condition)

# If only one kind of condition is required, pass [] for the other lists.

# A file descriptor is either a socket or file object, or a small integer gotten from a fileno() method call on one of those.

# The optional timeout argument specifies a time-out as a floating point number in seconds.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A time-out value of
