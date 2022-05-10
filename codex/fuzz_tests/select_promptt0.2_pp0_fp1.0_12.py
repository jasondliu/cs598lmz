import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# select() returns three lists of objects that are ready: subsets of the first three arguments.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A negative or None timeout means to block indefinitely.

# select() may modify the lists it receives as arguments, and may also return modified copies of the lists.

# select() should not be used if you can use poll() or epoll().

# select() supports operation on sockets, pipes and some other I/O objects.
# The file objects returned by open() and os.popen() and the stream objects returned by io.open() are not supported by select().

# select() is a useful tool for building multi-threaded network servers.
# It can be used to wait until a socket is ready for reading or writing, or until a
