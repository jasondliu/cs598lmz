import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if given, block until at least one file descriptor is ready or the timeout has elapsed

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sockets.
# It can also be used to wait for a file descriptor to become ready for some class of I/O operation (e.g., input possible).
# The following example shows how to multiplex input from two sockets and stdin.

# The select() function is a part of the POSIX standard, and is available on most Unix-like systems.
# On Windows, it is available as a part of the select module.

# The select() function takes three lists of
