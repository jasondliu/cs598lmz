import select
# Test select.select()
#
# A common use of select() is to multiplex input and output in a server.
# select() is told which file descriptors to watch.
#
# select() returns three lists of file descriptors.
# The first list contains descriptors that are ready for reading,
# the second contains descriptors that are ready for writing,
# and the third list is exceptional conditions.
#
# The server will have a socket open for listening to incoming connections,
# and it will have multiple other sockets that are connected to clients.
# select() will tell us when a socket is ready for reading or writing.
#
# This example uses TCP, but the same technique works for UDP.
#
# In the example, we have a listening socket ready for clients to connect.
# The server then waits in a select() call.
# When a client connects, the waiting is interrupted and we accept the connection.
# When we accept the connection, a new socket is returned.
# We set the new socket to non-blocking mode and add it to the list of sockets to watch.
#
# We then use a while loop to wait for activity on the sockets.
