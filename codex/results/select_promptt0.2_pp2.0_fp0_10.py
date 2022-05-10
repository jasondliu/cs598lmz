import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.poll()
# select.poll() is a cross-platform version of select() that works on many Unix platforms and on Windows.
# It supports registering multiple file descriptors to wait for.

# select.epoll()
# select.epoll() is available on Linux 2.6+
# It supports registering multiple file descriptors to wait for.

# select.kqueue()
# select.kqueue() is available on BSD and Mac OS X.
# It supports registering multiple file descriptors to wait for.

# select.devpoll()
# select.devpoll() is available on Solaris.
# It supports registering multiple file descriptors
