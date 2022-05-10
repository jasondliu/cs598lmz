import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# select() returns three lists of file descriptors: those that are ready for reading, those that are ready for writing, and those that have raised exceptions.

# select() will not necessarily return in exactly timeout seconds, as it does not have a very high resolution timer.

# select() can be interrupted by a signal (see the signal module) if the system supports restarting system calls.

# select() should not be used if you can use poll() or epoll().

# select() supports file descriptors greater than FD_SETSIZE, but some platforms select() silently ignore file descriptors in that range.

# select() is a useful tool for writing portable code, but it is not efficient.

# select() is not available on all platforms — if you need
