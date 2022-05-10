import select
# Test select.select()

# select.select() takes three lists of file descriptors and waits until
# some of them are ready for some kind of I/O.
# The first list is the list of file descriptors to be checked for being
# ready to read.
# The second list is the list of file descriptors to be checked for being
# ready to write.
# The third list is the list of file descriptors to be checked for error
# conditions.
# The return value is a triple of lists of file descriptors: subsets of the
# first three arguments.
# The first list returned contains the file descriptors that are ready for
# reading.
# The second list contains the file descriptors that are ready for writing.
# The third list contains the file descriptors that have an exceptional
# condition (out-of-band data available on TCP socket).

# The optional timeout argument specifies a time-out as a floating point
# number in seconds.
# When the time-out argument is omitted the function blocks until at least
# one file descriptor is ready.
# A time-out value of zero specifies a poll and never blocks.

# When
