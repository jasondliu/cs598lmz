import select
# Test select.select()

# The select() function takes three lists of file descriptors and waits until
# one or more of the descriptors is ready for some kind of I/O. The first list
# is watched to see if characters become available for reading (more precisely,
# to see if a read will not block - in particular, a file descriptor is also
# ready on end-of-file), the second list is watched to see if space is available
# for write, and the third list is watched for exceptions.

# The first three arguments to select() are sequences of file descriptors to be
# watched. These arguments are modified on return.

# The return value is a triple of lists of objects that are ready:
# (subset_of_read_list, subset_of_write_list, subset_of_except_list)

# The optional timeout argument specifies a time-out as a floating point number
# in seconds. When the timeout argument is omitted the function blocks until at
# least one file descriptor is ready. A time-out value of zero specifies a poll
# and never blocks.

# The select() function is a part of the POS
