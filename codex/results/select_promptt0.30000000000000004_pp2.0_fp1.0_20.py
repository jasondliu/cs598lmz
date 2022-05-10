import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# select() returns three lists of objects that are ready: subsets of the first three arguments.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A negative or None timeout means to block indefinitely.

# select() may modify the lists it receives as arguments, and may also return empty lists.

# The select() function is a direct interface to the underlying operating system implementation.
# It requires the caller to specify the number of open file descriptors, up to FD_SETSIZE,
# in the first three arguments. It also requires the caller to correctly size the timeout argument,
# which is an opaque object with no defined type.

# The poll() function supports a more flexible interface, and can be used on systems that do not support select().
# However, it does not support the full range of file
