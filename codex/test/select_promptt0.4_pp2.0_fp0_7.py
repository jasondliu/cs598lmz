import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition"
# timeout: in seconds

# Returns three lists of objects that are ready

# select.poll()
# select.epoll()
# select.kqueue()

# select.poll() is a cross-platform version of select.epoll()
# select.kqueue() is only available on BSD and OS X

# select.poll()
# Create a polling object
# poller = select.poll()
# Register a file descriptor
# poller.register(fd, eventmask)
# eventmask: POLLIN, POLLPRI, POLLOUT, POLLERR, POLLHUP, POLLNVAL
# poller.unregister(fd)
# poller.poll(timeout)
# timeout: in milliseconds
# Returns a list of (fd, event) tuples

# select.epoll()
# Create an epoll object
# epoll =
