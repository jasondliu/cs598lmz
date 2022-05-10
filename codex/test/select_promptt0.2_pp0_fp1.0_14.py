import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready
# If the time out period value is omitted the function blocks until at least one file descriptor is ready.
# A time out value of zero specifies a poll and never blocks.

# select.error: exception raised in case of an error.

# select.select() supports sockets, pipes and devices.

# select.poll()
# select.poll() is a more efficient way to wait for multiple file descriptors to become ready for I/O.
# select.poll() supports sockets, pipes and devices.

# select.epoll()
# select.epoll() is available on Linux 2.6+
# select.epoll() supports sockets, pipes and devices.

# select.kqueue()
# select.kqueue() is available on BSD and Mac OS X
