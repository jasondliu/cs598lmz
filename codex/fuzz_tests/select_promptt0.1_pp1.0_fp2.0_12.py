import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready
#
# Return value: three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready
#
# select.select() is a useful way to multiplex input from multiple sockets.
#
# The following example shows how to use select.select() to implement a simple echo server.
#
# The server uses select.select() to multiplex input from two sockets: one for the server itself, and one for each client.
#
# The server accepts a connection and then spawns a handler thread to deal with it.
#
# The handler thread reads input from the client and echoes it back.
#
# The handler thread terminates when the client closes the connection.
#
# The server terminates when a
