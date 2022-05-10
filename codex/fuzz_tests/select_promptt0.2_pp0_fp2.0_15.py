import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Returns three lists of objects that are ready: subsets of the first three arguments.

# When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

# When the time-out is reached with at least one file descriptor becoming ready, the time-out is reset to zero.

# When the optional time-out argument is absent or None, the function blocks until at least one file descriptor is ready.

# A file descriptor is considered ready if it is possible to perform the corresponding I/O operation (e.g., read(2) without blocking, or a sufficiently small write(2)).

# The file descriptor sets are modified in place to reflect the descriptors that are still in each set after the call.

# The following example shows how to use select() to monitor two sockets and standard input for input
