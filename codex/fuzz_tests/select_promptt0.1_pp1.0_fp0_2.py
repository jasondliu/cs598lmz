import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input/output over a set of file descriptors.
# It is the underlying mechanism for the high-level file object I/O functions.

# The select() function monitors a set of file descriptors for events.
# The set of file descriptors to be monitored is specified in three lists:
# readfds -- file descriptors to be checked for readiness to read
# writefds -- file descriptors to be checked for readiness to write
# errorfds -- file descriptors to be checked for error conditions
# The first three arguments to select() are the three lists of file descriptors to be monitored.
#
