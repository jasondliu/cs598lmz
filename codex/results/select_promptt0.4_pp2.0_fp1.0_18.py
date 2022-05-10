import select
# Test select.select()
# https://docs.python.org/3/library/select.html#select.select
# https://docs.python.org/3/library/select.html#select.poll

# The select() function monitors sockets, open files, and pipes (anything with a fileno() method that returns a valid file descriptor) until they become readable or writable, or a communication error occurs.

# The select() function is a higher-level wrapper that calls poll() and then does some filtering and updating of the results.

# select.select(rlist, wlist, xlist[, timeout])
# Wait until one or more file descriptors are ready for some kind of I/O. 
# The first three arguments are sequences of file descriptors to be waited for: rlist -- wait until ready for reading wlist -- wait until ready for writing xlist -- wait for an ``exceptional condition'' (see the manual page for what your system considers such a condition)
# If only one kind of condition is required, pass [] for the other lists.
# A file descriptor is either a socket or file object, or a small integer gotten from a fileno() method
