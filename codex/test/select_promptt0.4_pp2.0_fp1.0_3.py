import select
# Test select.select()

# select.select() takes three lists of sockets, waits until one or more of the sockets is ready for some kind of I/O, and returns a subset of those sockets.

# The first list, read_list, contains the sockets we're interested in reading from.
# The second list, write_list, contains the sockets we're interested in writing to.
# The third list, error_list, contains the sockets we're interested in knowing about errors on.
# The return value is a tuple of three lists, containing subsets of the lists we passed in.
# The first list contains the sockets ready for reading, the second contains the sockets ready for writing, and the third contains the sockets with errors.

# If you pass in an empty list for all three of these parameters, select.select() will wait forever.
# If you pass in an empty list for the first two parameters, but a socket or sockets in the error list, select.select() will return immediately.

# To wait until a socket is ready to accept a new connection, you would do this:

# read_list = [server_socket]
# write_list = []
#
