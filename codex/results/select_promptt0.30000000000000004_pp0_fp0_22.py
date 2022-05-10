import select
# Test select.select()
# select.select([rlist], [wlist], [xlist], timeout=None)
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready
# return value: 3 lists of objects that are ready

# select.poll()
# select.poll() returns a poll object, which supports registering and unregistering file descriptors, and then polling them for I/O events.
# poll.poll(timeout)
# poll.register(fd, eventmask)
# poll.unregister(fd)
# poll.modify(fd, eventmask)
# poll.close()
# eventmask: POLLIN, POLLOUT, POLLERR, POLLHUP, POLLNVAL
# return value: a list of (fd, event) 2-tuples

# select.epoll()
# select.epoll() returns an epolling object, which supports registering and un
