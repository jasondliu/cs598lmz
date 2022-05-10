import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
#
# If a file descriptor is ready for a given I/O operation, it is added to the corresponding list.
#
# To wait for a file descriptor to become ready for reading, use select() with the first argument as rlist.
#
# To wait for a file descriptor to become ready for writing, use select() with the first argument as wlist.
#
# To wait for a file descriptor to have an exceptional condition pending, use select() with the first argument as xlist.
#
# The timeout argument specifies the maximum time to wait for a file descriptor to become ready.
# If timeout is None, select() can block indefinitely.
# If timeout is zero, select() returns immediately, even if no file descriptors are ready.
#
# If the return value is three empty lists, the timeout expired before anything happened.
# If the return value contains one or more file descriptors, they are ready for the corresponding I/O operation.
#
# The following example waits for a file descriptor to become ready for reading or writing, or until a timeout occurs:
#

