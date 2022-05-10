import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not supplied, block until a monitored file descriptor becomes ready; if supplied as a float, it specifies a timeout in seconds; as a tuple of two floats, the first is a timeout in seconds and the second is a timeout in microseconds

# select.select() returns three lists of objects that are ready: subsets of the first three arguments. When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

# select.select() supports a timeout, which is a floating point number specifying a time-out as a number of seconds. When the timeout argument is omitted the function blocks until at least one file descriptor is ready. A time-out value of zero specifies a poll and never blocks.

# select.select() may modify the lists it receives as arguments, and may also return modified copies of the lists.

# select
