import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: a time-out as a floating point number in seconds (or None for no time-out)

# select() returns three lists of objects that are ready: subsets of the first three arguments.
# When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.
# A file descriptor is considered ready if it is possible to perform the corresponding I/O operation (e.g., read(2) without blocking, or a sufficiently small write(2)).

# select() may modify the timeout argument.

# select() can be interrupted by a signal (see signal(7)) and return EINTR;
# in this case the caller should repeat the select() call.
# If select() is interrupted by a signal handler, and the time-out expires before the signal handler returns,
# then select() returns with
