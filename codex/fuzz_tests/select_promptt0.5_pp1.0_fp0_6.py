import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)

# If the timeout is omitted, select() can block indefinitely.
# If the timeout is zero, it will not block at all, but will return the current state of the file descriptor set.
# If the timeout is nonzero, it will block until a file descriptor is ready or the timeout has elapsed.
# The return value is a triple of lists of objects that are ready: subsets of the first three arguments.
# When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

# When select() returns, the results array contains the subset of the requested file descriptors that are ready.
# For each file descriptor less than nfds, the corresponding bit will be set if that file is ready for the requested operation.
# Thus, after select() returns, for each file descriptor fd with revents & POLLIN set,
