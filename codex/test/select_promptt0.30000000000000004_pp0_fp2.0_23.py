import select
# Test select.select()

# select.select() takes three lists of file descriptors,
# and waits until one or more of the file descriptors is ready for some kind of I/O.
# The first list contains the file descriptors to be checked for being readable,
# the second contains the file descriptors to be checked for being writable,
# and the third contains the file descriptors to be checked for error conditions.
# The return value is a triple of three lists of file descriptors;
# each list contains the subset of the corresponding file descriptors that are ready.

# The first list contains the file descriptors to be checked for being readable,
# the second contains the file descriptors to be checked for being writable,
# and the third contains the file descriptors to be checked for error conditions.

# The return value is a triple of three lists of file descriptors;
# each list contains the subset of the corresponding file descriptors that are ready.

# The optional timeout argument specifies a time-out as a floating point number in seconds.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A time-out
