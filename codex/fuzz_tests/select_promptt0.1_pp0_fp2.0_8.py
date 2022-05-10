import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.error: exception raised in case of an error

# select.select() can be used to monitor multiple sockets at the same time
# select.select() is a blocking call

# select.poll()
# select.poll() is a non-blocking version of select.select()
# select.poll() returns a dictionary-like object that maps file descriptors to events
# select.poll() is available on Unix and Windows systems

# select.epoll()
# select.epoll() is available on Linux systems
# select.epoll() is a more efficient version of select.poll()
# select.epoll() is a non-blocking version of select.select()
# select.epoll() returns a dictionary-like object that maps file descriptors to events
