import select
# Test select.select
# https://docs.python.org/2/library/select.html

# select.select(rlist, wlist, xlist[, timeout])
# Wait until one or more file descriptors are ready for some kind of I/O
# The first three arguments are sequences of file descriptors to be waited for:
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# If only one kind of condition is required, pass [] for the other lists.

# A file descriptor is ready if it is possible to perform the corresponding I/O operation (e.g., read(2) without blocking, or a sufficient buffer being available for write(2))

# The optional timeout argument specifies a time-out as a floating point number in seconds. When the timeout argument is omitted the function blocks until at least one file descriptor is ready. A time-out value of zero specifies a poll and never blocks.

# The return value is a triple of lists of objects that are ready: sublists corresponding
