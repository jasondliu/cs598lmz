import select
# Test select.select()

# select.select()
# select.select(rlist, wlist, xlist[, timeout])
#
# Wait until one or more file descriptors are ready for some kind of I/O.
# The first three arguments are sequences of file descriptors to be waited for:
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
#
# If only one kind of condition is required, pass [] for the other lists.
#
# A file descriptor is either a socket or file object, or a small integer
# gotten from a fileno() method call on one of those.
#
# The optional timeout argument specifies a time-out as a floating point number in seconds.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A time-out value of zero specifies a poll and never blocks.
#
# The return value is a triple of lists of objects that are ready:
# (subset of rlist, subset of w
