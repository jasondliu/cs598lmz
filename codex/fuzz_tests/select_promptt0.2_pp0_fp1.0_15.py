import select
# Test select.select()

# select.select() takes three lists of file descriptors and waits until
# some of them are ready for some kind of I/O.
# The first list is the list of file descriptors to be checked for being
# ready to read, the second list is the list of file descriptors to be
# checked for being ready to write, and the third list is the list of
# file descriptors to be checked for error conditions.
# The return value is a triple of lists of file descriptors; the first
# list contains the subset of the first argument that is ready for reading,
# the second list contains the subset of the second argument that is ready
# for writing, and the third list contains the subset of the third argument
# that has an exceptional condition pending.

# The optional timeout argument specifies a time-out as a floating point
# number in seconds. When the timeout argument is omitted the function
# blocks until at least one file descriptor is ready. A time-out value of
# zero specifies a poll and never blocks.

# When select() returns, the lists are updated to only contain the file
# descriptors that are still "ready".
