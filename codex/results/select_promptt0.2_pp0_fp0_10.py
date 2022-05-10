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
# The return value is a triple of lists of file descriptors; the first
# list contains the subset of the first three arguments that are ready
# for reading, the second contains the subset that are ready for writing,
# and the third contains the subset that have an exceptional condition.

# The optional timeout argument specifies a time-out as a floating point
# number in seconds. When the timeout argument is omitted the function
# blocks until at least one file descriptor is ready. A time-out value of
# zero specifies a poll and never blocks.

# The return value is a triple of lists of file descriptors; the first
# list contains the subset of the first three arguments that are ready
# for reading
