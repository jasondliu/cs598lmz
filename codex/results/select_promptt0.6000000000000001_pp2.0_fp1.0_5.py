import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist -- wait until ready for reading
# wlist -- wait until ready for writing
# xlist -- wait for an "exceptional condition" (see below)
#
# All three lists are optional and may be empty. If all three lists are empty,
# select() will return an empty list.
#
# The optional timeout argument specifies a time-out as a floating point
# number in seconds. When the timeout argument is omitted the function will
# block until at least one file descriptor is ready. A time-out value of zero
# specifies a poll and never blocks.
#
# A time-out value of None specifies an unbounded wait.
#
# The return value is a triple of lists of objects that are ready:
#  sublists for reading, writing, and errors.
#
# The input lists are modified to remove the file descriptors that are ready.
#
# Exceptional conditions:
#
#  * EBADF -- file descriptor is not open
#  * EINTR -- interrupted by a signal
#
