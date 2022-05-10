import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until ready

# The return value is a triple of lists of objects that are ready:
# sublists corresponding to the sequences of waitables passed to the function as rlist, wlist, and xlist.
# If the time-out is reached without a file descriptor becoming ready, three empty lists are returned.
# Note that on Windows, only sockets are supported; on Unix, all file descriptors can be used.

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until ready

# The return value
