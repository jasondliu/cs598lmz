import select
# Test select.select()

# Returns a list of file descriptors that are ready for some I/O operation
# The first parameter is a list of file descriptors to monitor for input
# The second parameter is a list of file descriptors to monitor for output
# The third parameter is a list of file descriptors to monitor for errors
# The fourth parameter is the timeout
# If a file descriptor is ready for an I/O operation, it is added to the list
# returned by select()

# For example, if the first file descriptor is ready for input, it is added to
# the list returned by select()

# select() returns a list of file descriptors that are ready for some I/O
# operation

# select() takes a timeout value in seconds. If the timeout value is 0, then
# select() will return immediately. If the timeout value is None, then select()
# will block until an event occurs.

# If the timeout value is negative, then select() will block indefinitely until
# an event occurs

# If a file descriptor is ready for an I/O operation, it is added to the list
# returned by select()

# If
