import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if a positive number, block at most that many seconds and return three empty lists if no file descriptor is ready
# Return value: three lists of file descriptors: rlist, wlist, xlist
# select.select(rlist, wlist, xlist[, timeout])

# select.poll()
# select.poll()
# Return a polling object, which supports registering and unregistering file descriptors, and then polling them for I/O events.
# select.poll()

# select.epoll()
# select.epoll()
# Return an epolling object, which supports registering and unregistering file descriptors, and then polling them for I/O events.
# select.epoll()

#
