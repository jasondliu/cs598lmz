import select
# Test select.select
# select.select(r, w, e, timeout=None)
# r = list of sockets to read from
# w = list of sockets to write to
# e = list of sockets to check for exceptions
# timeout = timeout in seconds
# returns 3 lists of sockets ready for the specified I/O
# if timeout is omitted, will block until a socket is ready

# Test select.poll
# select.poll()
# returns a poll object
# poll.register(fd, eventmask)
# poll.modify(fd, eventmask)
# poll.unregister(fd)
# poll.poll(timeout=None)
# returns a list of (fd, event) pairs

# Test select.epoll
# select.epoll(sizehint=0)
# returns an epoll object
# epoll.fileno()
# returns the file descriptor
# epoll.register(fd, eventmask)
# epoll.modify(fd, eventmask)
# epoll.unregister(fd)
# epoll.poll(timeout=None)
# returns a list of (fd, event) pairs
