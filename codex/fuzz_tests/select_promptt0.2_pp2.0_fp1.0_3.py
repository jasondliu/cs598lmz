import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready
# rlist: objects in rlist that are ready for reading
# wlist: objects in wlist that are ready for writing
# xlist: objects in xlist that have an “exceptional condition”

# select.error: If a file descriptor is given in an invalid range (less than zero or greater than FD_SETSIZE, the maximum number of file descriptors), select() raises an exception.

# select.select() is a blocking call.

# select.select() is available on Unix and Windows.

# select.select() monitors sockets, open files, and pipes (anything with a fileno() method that returns a valid file descriptor).

# select.select() can monitor sockets for
