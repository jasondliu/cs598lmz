import select
# Test select.select()
# select.select() is a blocking function.
# It will wait until the file descriptor is readable or writable.
# The first parameter is a list of file descriptors to check for readability.
# The second parameter is a list of file descriptors to check for writability.
# The third parameter is a list of file descriptors to check for errors.
# The fourth parameter is a timeout in seconds.
# If the timeout is 0, then select() will return immediately.
# If the timeout is negative, then select() will block indefinitely.
# The return value is a tuple of three lists.
# The first list contains the file descriptors that are readable.
# The second list contains the file descriptors that are writable.
# The third list contains the file descriptors that have errors.
# The file descriptors that are returned are not guaranteed to be in any particular order.
# If select() returns an empty list for all three lists, then the timeout has occurred.
# If select() returns a list for one or more of the three lists, then the timeout has not occurred.
# The timeout is only an estimate.
# It is not guaranteed to
