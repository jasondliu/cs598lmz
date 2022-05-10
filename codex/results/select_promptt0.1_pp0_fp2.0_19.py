import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.error: exception raised in case of an error

# select.select() can be used as a way to implement a timeout on blocking I/O operations like the kind that can be done with a socket.

# select.select() is also useful for handling multiple channels of communication “simultaneously”.

# select.select() is available on Unix and on Windows.

# select.poll() is available on Unix and Windows.

# select.epoll() is available on Unix.

# select.kqueue() is available on BSD.

# select.kevent() is available on BSD.

# select.devpoll() is available on Solaris.

# select.select() is the most portable of these, but it is
