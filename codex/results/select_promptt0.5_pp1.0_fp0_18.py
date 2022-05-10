import select
# Test select.select()
# https://docs.python.org/3/library/select.html

# select.select() takes three lists of file descriptors and waits until
# one or more of the descriptors are ready for some kind of I/O.
# The first list is the list of file descriptors to be checked for being
# ready to read.
# The second list is the list of file descriptors to be checked for being
# ready to write.
# The third list is the list of file descriptors to be checked for errors.

# The return value is a three-element tuple containing lists of the
# subset of the first three arguments that are ready for I/O.

# If the timeout is zero, then select() will return immediately,
# with all three lists empty.

# If the timeout is negative, then select() will block until an event
# happens on one of the descriptors.

# If the timeout is positive, then select() will block until either an
# event happens on one of the descriptors or the timeout period has
# elapsed.
# The return value is a tuple of three lists of file descriptors.
#
