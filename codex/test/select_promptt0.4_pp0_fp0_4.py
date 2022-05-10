import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified or None, block until a file descriptor is ready. If specified as a floating point number, it specifies a timeout in seconds (for example, 0.1)
#
# select() returns three lists of objects that are ready: subsets of the first three arguments. When the timeout argument is omitted it will block until at least one file descriptor is ready. A file descriptor is considered ready if it is possible to perform the corresponding I/O operation (e.g., read(2)) without blocking.
#
# When the timeout argument is present and not None, it should be a floating point number specifying a timeout for the operation in seconds (or fractions thereof).
#
# The return value is a triple of lists of objects that are ready: subsets of the first three arguments. When the timeout argument is omitted the call will block until at
