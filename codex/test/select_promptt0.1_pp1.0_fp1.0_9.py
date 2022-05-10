import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select.select() is a blocking call.
# If a timeout is given and no file descriptor is ready, the call will block for at most timeout seconds.
# If the timeout is reached, three empty lists are returned.
# If the timeout is zero, then select() will never block.

# select.select() is available on Unix and Windows.
# On Unix, it supports file descriptors, as well as sockets.
# On Windows, it only supports sockets.

# select.select() is a useful way to multiplex input from multiple sources.
# It is also useful for implementing a timeout on blocking I/O operations.

# Example:
# A simple echo server using select.select
