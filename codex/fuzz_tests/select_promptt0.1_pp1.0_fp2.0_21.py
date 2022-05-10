import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input/output over a number of sockets or other file-like objects.

# select.select() is available on Unix and Windows.

# select.poll() is available on Unix and Windows.

# select.epoll() is available on Unix.

# select.kqueue() is available on BSD.

# select.kevent() is available on BSD.

# select.devpoll() is available on Solaris.

# select.select() is a useful way to multiplex input/output over a number of sockets or other file-like objects.

# select.select() is available on Unix and Windows.

