import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select.poll()
# select.poll() is a cross-platform version of select() that works on many Unix platforms and on Windows.
# It supports the same operations as select(), but it does not have a timeout parameter.
# Instead, you register a file descriptor with the poll object, and then call the poll object’s poll() method.
# The poll() method returns a list of (fd, event) tuples, where fd is a file descriptor, and event is an event mask of the operations that are ready.
# The event mask can be constructed by performing a bitwise OR of constants such as select.POLLIN, select.POLLOUT, and select.POLLERR.

