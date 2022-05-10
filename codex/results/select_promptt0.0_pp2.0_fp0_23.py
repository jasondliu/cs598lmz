import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output, especially when there are many connections to monitor.
# It is also a way to implement asynchronous I/O in Python.

# select.select() is available on Unix and Windows.

# select.poll() is available on Unix and Windows.

# select.epoll() is available on Unix.

# select.kqueue() is available on BSD.

# select.devpoll() is available on Solaris.

# select.select() is the most portable of these options.

# select.select() is a useful way to multiplex input and output, especially when there
