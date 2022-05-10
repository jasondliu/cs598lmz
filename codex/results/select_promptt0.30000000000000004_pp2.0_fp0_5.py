import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# The optional timeout argument specifies a time-out as a floating point number in seconds. When the timeout argument is omitted the function blocks until at least one file descriptor is ready. A time-out value of zero specifies a poll and never blocks.

# The return value is a tuple of three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready.

# When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

# A file descriptor is considered ready if it is possible to perform the corresponding I/O operation (e.g., read(2) without blocking, or a sufficiently small write(2)).

# The following example illustrates the typical use of select() in a server:

# import select
#
