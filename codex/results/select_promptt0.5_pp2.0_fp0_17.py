import select
# Test select.select()
# https://docs.python.org/2/library/select.html#select.select

# select.select(rlist, wlist, xlist[, timeout])
# Wait until one or more file descriptors are ready for some kind of I/O.
# The first three arguments are sequences of file descriptors to be waited for: rlist --
# wait until ready for reading, wlist -- wait until ready for writing, xlist -- wait for
# an ``exceptional condition'' (see the manual page for what your system considers
# such a condition). All three arguments must be sequences of the same length.

# timeout is an optional float giving a timeout for the operation in seconds (or fractions
# thereof). If it is absent or None, the call will never time out.

# The return value is a tuple of three lists corresponding to the first three arguments;
# each contains the subset of the corresponding file descriptors that are ready. When
# the time-out is reached without a file descriptor becoming ready, three empty lists are
# returned.

# A file descriptor is considered ready if it is possible to perform the corresponding
# I/
