import select
# Test select.select

# https://docs.python.org/3/library/select.html

# select.select(rlist, wlist, xlist[, timeout])

# Wait until one or more file descriptors are ready for some kind of I/O. The first three arguments are sequences of file descriptors to be waited for: rlist – wait until ready for reading, wlist – wait until ready for writing, xlist – wait for an “exceptional condition” (see the manual page for what your system considers such a condition).

# All three arguments must be sequences of the same length with the corresponding descriptors from each sequence paired together (that is, rlist[0] with wlist[0] and xlist[0]). The result is a tuple with three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready.

# The optional timeout argument specifies a time-out as a floating point number in seconds. When the timeout argument is omitted the function blocks until at least one descriptor is ready. A time-out value of zero specifies a poll and never blocks.

# The return value is a triple of lists of objects
