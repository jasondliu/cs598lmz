import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready
# Return value: three lists of objects that are ready

# select.poll()
# select.poll()
# Return value: a polling object
# poll.register(fd[, eventmask])
# fd: file descriptor
# eventmask: events to check for
# Return value: None
# poll.unregister(fd)
# fd: file descriptor
# Return value: None
# poll.poll(timeout)
# timeout: if not specified, will block until a monitored file descriptor becomes ready
# Return value: a list of (fd, event) 2-tuples

# select.epoll()
# select.epoll()
# Return value: an epolling object
# epoll.register(fd[, eventmask])

