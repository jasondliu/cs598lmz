import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready
#
# Returns three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready.
#
# A file descriptor is considered ready if it is possible to perform the corresponding I/O operation (e.g., read(2)) without blocking.
#
# The file descriptors to be monitored are specified in three lists: rlist, wlist, and xlist.
#
# The first three arguments are sequences of file descriptors to be waited for:
# rlist -- wait until ready for reading
# wlist -- wait until ready for writing
# xlist -- wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
#
# The optional fourth argument specifies a timeout in seconds
