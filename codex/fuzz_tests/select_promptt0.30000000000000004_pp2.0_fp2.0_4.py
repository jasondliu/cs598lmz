import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
#
# The return value is a tuple of three lists corresponding to the first three arguments; each contains the subset of the
# corresponding file descriptors that are ready.
#
# The optional timeout argument specifies a time-out as a floating point number in seconds. When the timeout argument is
# omitted the function blocks until at least one file descriptor is ready. A time-out value of zero specifies a poll and
# never blocks.
#
# When the timeout argument is present and not None, it should be a floating point number specifying a timeout for the
# operation in seconds (or fractions thereof).
#
# The return value is a triple of lists of objects that are ready: subsets of the first three arguments. When the time-out
# is reached without a file descriptor becoming ready, three empty lists are returned.
#
# A file descriptor is
