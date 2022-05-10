import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not supplied, block until a monitored file descriptor becomes ready; if supplied as a float, it specifies a timeout in seconds; as a tuple of integers, it specifies a timeout as an (seconds, microseconds) pair
# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.poll()
# select.poll() is a cross-platform alternative to select() available on Unix and Windows. It supports registering multiple file descriptors to wait for them to become ready for I/O.

# select.poll() returns a poll object, which supports registering and unregistering file descriptors, and then polling them for I/O events.

# select.poll() is available on Unix and Windows.

# select.epoll()
# select.epoll() is a Linux-only alternative to select
