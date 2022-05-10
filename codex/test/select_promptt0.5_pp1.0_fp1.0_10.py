import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# Return three lists of objects that are ready for input, output, and error.
# The first three arguments are sequences of objects to be waited for:
# rlist is waited for input, wlist for output, and xlist for errors.
# These are all optional, and default to [], [], [].
# The optional timeout argument specifies a time-out as a floating point number in seconds.
# When the timeout argument is omitted the function blocks until at least one of the objects is ready.
# A time-out value of zero specifies a poll and never blocks.
# A negative value specifies an infinite wait.
# The return value is a tuple of three lists containing the subset of the corresponding sequence arguments that are ready.
# When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.
#
# select.select(rlist, wlist, xlist[, timeout])
# Wait until one or more file descriptors are ready for some kind of I/O.
# The first three arguments are sequences of file descriptors to be waited for:
