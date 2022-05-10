import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist, wlist, xlist are lists of file descriptors to be waited for
# timeout is an optional timeout value in seconds
# Returns three lists of file descriptors: those that are ready for reading, writing, and those that have an exception pending
# If the timeout is omitted, it will block until at least one file descriptor is ready

# Test select.poll()
# select.poll()
# Returns a polling object, which supports registering and unregistering file descriptors, and polling them for I/O events
# poll.register(fd[, eventmask])
# fd is the file descriptor to be registered
# eventmask is a bitmask of events to be monitored
# poll.unregister(fd)
# fd is the file descriptor to be unregistered
# poll.poll(timeout)
# timeout is an optional timeout value in milliseconds
# Returns a list of (fd, event) tuples

# Test select.epoll()
# select.epoll()
# Returns an epolling object, which supports registering and unregistering file
