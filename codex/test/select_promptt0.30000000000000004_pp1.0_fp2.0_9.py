import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Returns three lists of subset of the first three arguments: those descriptors that are ready, those that have an exceptional condition, and those that have timed out.

# If only one kind of condition is required, pass [] for the other lists. If no timeout is required, pass None for the timeout.

# If the timeout is zero, then select() will return immediately, without blocking.

# The select() function is a direct interface to the underlying operating system implementation. It does not modify the timeout argument.

# The return value is a triple of lists of objects that are ready: subsets of the first three arguments. When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

# When the time-out is zero, select() can be used as a polling function, checking to see if a given file descriptor is
