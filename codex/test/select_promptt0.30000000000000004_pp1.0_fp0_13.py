import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
#
# The return value is a triple of lists of objects that are ready:
# (subset of rlist, subset of wlist, subset of xlist)
#
# If the time-out is reached without a file descriptor becoming ready, three empty lists are returned.
#
# The time-out argument is a floating point number expressed in seconds.
# When the time-out argument is omitted the function blocks until at least one file descriptor is ready.
# A time-out value of zero specifies a poll and never blocks.
#
# The objects that are returned are always subset of the lists that were given as arguments.
#
# The objects in the lists are file descriptors, which are small integers.
#
# The file descriptor lists are modified in place (since they are passed by reference).
#
# The file descriptor lists
