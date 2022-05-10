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
# sockets while a server handles multiple clients at the same time.

# The server creates a TCP/IP socket and listens for connections.
# The server accepts a connection with the accept() system call.
# The connection is actually a different socket on another port.
# The server can now receive data from the client by reading from the
# socket.
# The server can also send data to the client by writing to the socket.
# The server closes the connection with the close
