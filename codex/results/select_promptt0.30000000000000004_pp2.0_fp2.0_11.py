import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.error: exception raised for invalid file descriptors

# select.select() supports sockets, pipes, and devices.

# select.poll()
# select.poll() is a more efficient way to wait for multiple I/O events.

# select.poll() supports sockets, pipes, and devices.

# select.poll() is only supported on systems with a /dev/poll or epoll(4) interface.

# select.poll() is available on most Unix systems.

# select.poll() is not available on Windows.

# select.poll() is not available on Mac OS X.

# select.poll() is available on Linux.

# select.poll() is available on Solaris.

# select.poll() is available
