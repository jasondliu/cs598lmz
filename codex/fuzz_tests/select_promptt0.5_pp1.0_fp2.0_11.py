import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
#
# Returns three lists of objects that are ready: subsets of the first three arguments.
#
# The optional timeout argument specifies a time-out as a floating point number in seconds. When the time-out period
# expires, three empty lists are returned.
#
# A time-out value of zero specifies a poll and never blocks.
#
# The select() function can be interrupted by a signal (see the signal module). In that case, it returns three
# empty lists.
#
# select() should not be used if you need a timeout that is related to a real time clock. Use poll() or epoll() as
# they depend on a monotonic clock.
#
# The most portable way is to use select() on all file descriptors, and then to use recv() without the MSG_DONTWAIT
