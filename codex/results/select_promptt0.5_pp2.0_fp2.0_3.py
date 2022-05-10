import select
# Test select.select
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: waits until ready for reading
# wlist: waits until ready for writing
# xlist: waits for an "exceptional condition" (see the manual for more info)
#
# Note:
# You can use select to multiplex many file descriptors, waiting until
# one or more of the file descriptors become "ready" for some class of I/O
# operation (e.g., input possible).
#
# Returns three lists of file descriptors:
# rlist -- list of file descriptors that are ready for reading
# wlist -- list of file descriptors that are ready for writing
# xlist -- list of file descriptors that have raised exceptions
#
# The optional timeout argument specifies a time-out as a floating point
# number in seconds. When the timeout argument is omitted the function blocks
# indefinitely.
#
# A time-out value of zero specifies a poll and never blocks.
#
# The return value is a triple of lists of objects that are ready:
# either for reading, writing or in an
