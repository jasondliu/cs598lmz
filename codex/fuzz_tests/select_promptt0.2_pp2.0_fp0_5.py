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

# The following example shows how to use select() to monitor a pair of
# sockets and stdin for input.

# This example uses a server and client pair running on the local host.
# The server listens for connections on port 8080 and echoes back whatever
# it receives.
# The client connects to the server, sends some text, and exits.
# The server and client are implemented in the same program.
# The server runs in a separate thread.
# The main thread accepts input from stdin and sends it to the server
