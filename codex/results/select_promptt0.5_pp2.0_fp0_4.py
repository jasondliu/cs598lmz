import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist, wlist, xlist: sequence of file descriptors to be checked
# timeout: time to wait for a response, in seconds
# returns: a tuple of three lists of file descriptors (rlist, wlist, xlist)
# that are ready for reading, writing, or have an exception pending

# select.error: exception raised by select()

# select.poll(): a class implementing a portable interface to the system
# select() function

# select.poll.poll([timeout]): returns a list of (fd, event) tuples
# fd: file descriptor
# event: a bitmask of events

# select.poll.register(fd[, eventmask]): register a file descriptor with
# the polling object
# fd: file descriptor
# eventmask: a bitmask of events
# returns: None

# select.poll.unregister(fd): unregister a file descriptor
# fd: file descriptor
# returns: None

# select.poll.modify(fd, eventmask): modify a
