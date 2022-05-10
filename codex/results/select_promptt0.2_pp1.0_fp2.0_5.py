import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.select() is a blocking call.
# It waits until at least one of the descriptors is ready for some kind of I/O.
# The first three arguments are sequences of file descriptors to be waited for:
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# The optional timeout argument specifies a time-out as a floating point number in seconds.
# When the timeout argument is omitted the function blocks until at least one descriptor is ready.
# A time-out value of zero specifies a poll and never blocks.

# The return value is a triple of lists of objects that are ready:

