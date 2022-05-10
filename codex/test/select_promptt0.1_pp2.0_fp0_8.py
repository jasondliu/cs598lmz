import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select() can be used to implement a timeout on I/O operations in a portable way.
# If the timeout is omitted, select() can block indefinitely.

# select() can also be used to implement a simple event loop.
# The select() function is a way to poll the operating system to see if any file descriptors have changed status.
# The select() function takes three lists of file descriptors:
# the first is a list of file descriptors to be checked for being ready to read,
# the second is a list of file descriptors to be checked for being ready to write,
# and the third is a list of file descriptors to be checked for error
