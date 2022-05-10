import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until at least one file descriptor is ready; if specified as a float, will block that many seconds; if specified as None, will block indefinitely
#
# Returns three lists of objects that are ready: subsets of the first three arguments.
#
# If the time out period value is reached and no file descriptors are ready, three empty lists are returned.
#
# The optional timeout argument specifies a time-out as a floating point number in seconds. When the timeout argument is omitted the function blocks until at least one file descriptor is ready. A time-out value of zero specifies a poll and never blocks.
#
# The return value is a triple of lists of objects that are ready: subsets of the first three arguments. When the time-out is reached without a file descriptor becoming ready, three empty lists are
