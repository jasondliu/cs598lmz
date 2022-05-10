import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: is a float expressing seconds, or None. If None, block until a monitored file descriptor becomes ready.
# Returns three lists of objects that are ready: subsets of the first three arguments.

# select.poll()
# select.poll() is a cross-platform equivalent to select() that works on many Unix platforms and on Windows.

# select.epoll()
# select.epoll() is a more efficient way to wait for I/O completion on Linux 2.5.44 and newer.

# select.kqueue()
# select.kqueue() is a more efficient way to wait for I/O completion on BSD.

# select.devpoll()
# select.devpoll() is a more efficient way to wait for I/O completion on Solaris.

# select.kevent()
# select
