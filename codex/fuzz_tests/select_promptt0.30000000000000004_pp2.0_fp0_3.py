import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until ready

# Return value: three lists of objects that are ready

# select.poll()
# select.poll() is a cross-platform alternative to select()
# It is more efficient because it doesn’t have to copy the lists of file descriptors
# It is also more flexible because you can register a callback function to be called when a file descriptor is ready

# select.epoll()
# select.epoll() is available on Linux systems
# It is more efficient than select.poll()
# It is also more flexible because you can register a callback function to be called when a file descriptor is ready

# select.kqueue()
# select.kqueue() is available on BSD systems
# It is more efficient than select.poll()
# It is also more flexible because you
