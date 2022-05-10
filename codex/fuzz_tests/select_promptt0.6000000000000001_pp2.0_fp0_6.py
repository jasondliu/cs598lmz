import select
# Test select.select()
print 'Testing select.select()'
# First argument is a list of lists, each list containing a socket object
# and the events to be monitored on that socket.
# Second argument is a list of lists, each list containing a socket object
# and the events that occurred on that socket.
# The return value is a tuple containing three lists, each list containing
# a socket object and the events that occurred on that socket.
# The third argument is the timeout.
# The first list contains all of the ready sockets,
# the second list contains all of the sockets with errors,
# and the third list contains all of the sockets that were
# not ready before the timeout expired.

# The events that can occur on a socket are:
# select.POLLIN: There is data to be read.
# select.POLLPRI: There is urgent data to be read.
# select.POLLOUT: Writing to the socket won't block.
# select.POLLERR: The socket has an error.
# select.POLLHUP: The socket has been hung up on.
# select.POLLNVAL: The file descriptor
