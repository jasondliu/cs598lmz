import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments.

# select.select() is a useful way to multiplex input from multiple sources.

# select.select() is available on Unix and Windows systems.

# select.select() monitors sockets, open files, and pipes (anything with a fileno() method that returns a valid file descriptor) until they become readable or writable or a communication error occurs.

# select.select() can also be used to monitor multiple pipes at once, doing a simple form of I/O multiplexing.

# select.select() can be used to implement a timeout while waiting for I/O completion.

# select.select() is the most portable way to implement timeout functionality in Python.
