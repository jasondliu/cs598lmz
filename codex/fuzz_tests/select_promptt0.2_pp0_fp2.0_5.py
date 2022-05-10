import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# Timeout is in seconds; can be a float. If None, will block until a monitored file descriptor becomes ready.

# select.select() is a useful way to multiplex input/output over a number of sockets or other file-like objects.

# The following example shows how to use select() to monitor a number of sockets (including standard input) for activity.

# The example is a chat server, which accepts connections on port 5000.

# The server broadcasts any messages from a client to all other clients.

# The server handles each client in a separate thread.

# The client is a simple terminal chat client, which also accepts input from standard input, so that the user can send messages to the server.

# The client can be terminated by typing “/quit
