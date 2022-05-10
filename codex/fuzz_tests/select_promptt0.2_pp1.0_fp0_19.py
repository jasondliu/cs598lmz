import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sources.

# Example:
# The following example shows how to use select() to monitor a pair of sockets and stdin for input at the same time.
# It uses the select() to wait until either a socket is ready to read, or stdin is ready to read.
# If a socket is ready, it accepts a new connection and adds the socket to the list of sockets to be monitored.
# If stdin is ready, it reads a line of input and echoes it back to the client.

# This example is not robust: it doesn’t handle errors, it echoes all received data back
