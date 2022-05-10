import select
# Test select.select()

# select.select() takes three lists of file descriptors:
#   1. A list of file descriptors to watch for being "ready for reading"
#   2. A list of file descriptors to watch for being "ready for writing"
#   3. A list of file descriptors to watch for errors
# It returns three lists of file descriptors:
#   1. Those from the first list that are ready for reading
#   2. Those from the second list that are ready for writing
#   3. Those from the third list that have errors

# select.select() blocks until at least one file descriptor is ready.
# If a file descriptor is ready, it is returned in the corresponding list
# (even if it is also ready for the other operations).
# If more than one file descriptor is ready, they are all returned.
# If a file descriptor is not ready, it is not returned in any list.

# The timeout argument is the maximum time to wait, in seconds.
# If timeout is None, select.select() blocks until at least one file descriptor is ready.
# If timeout is 0.0, it does not
