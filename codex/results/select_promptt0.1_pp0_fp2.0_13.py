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
# The return value is a triple of lists of file descriptors: the subset of
# the first three parameters that are ready for the corresponding I/O
# operations.

# The following example shows how to use select() to monitor multiple
# sockets.

# The example is a simple echo server. It listens on two sockets, one for
# IPv4 and another for IPv6.

# The server handles each connection in a separate process.

# The server handles each connection in a separate thread.

# The server handles each connection in a separate coroutine.

# The server handles each connection in a separate coroutine.
# The coroutine is scheduled using the asyncio module.

#
