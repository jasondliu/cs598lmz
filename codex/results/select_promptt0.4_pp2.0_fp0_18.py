import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified (or 0 specified), block until ready; if specified, it is in seconds, and the function will return three empty lists if the timeout period value has elapsed before anything interesting happens

# select() returns three lists of objects that are ready: subsets of the first three arguments. When the return value is three empty lists, a timeout has occurred.

# When the specified time-out period value has elapsed, and nothing interesting has happened, select() returns three empty lists.

# When the specified time-out period value has elapsed, and one or more file descriptors become ready, select() returns the subset of those file descriptors that are ready.

# When the specified time-out period value has elapsed, and one or more exceptional conditions arise, select() returns the subset of those file descriptors that have an exceptional condition pending.

#
