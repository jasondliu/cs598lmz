import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select() should not be used if you can use poll() or epoll().
# select() is inefficient and does not scale well.

# select() supports file descriptors greater than FD_SETSIZE, but it does not support file descriptors greater than 1024 on Windows.
# On Windows, select() only works on sockets, and is limited to 64 sockets at a time.

# select() can be interrupted by a signal (such as SIGALRM).
# In that case, select() will return immediately with EINTR.
# If you want to be sure that select() won’t be interrupted, you can use a signal handler that does nothing but return,
# and set the signal to be ignored
