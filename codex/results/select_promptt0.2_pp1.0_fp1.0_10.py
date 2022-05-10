import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments
# If the time limit is reached with no file descriptors ready, three empty lists are returned

# select.select() is a useful way to multiplex input from multiple sources
# Example:
#   1. Wait for input on any of a set of sockets
#   2. Wait for data to be available for reading on a socket
#   3. Wait for a socket to be ready for writing
#   4. Wait for a socket to close
#   5. Wait for a socket to become available for accepting connections
#   6. Wait for a socket to become available for connecting
#   7. Wait for a socket to have urgent data available for reading
#   8. Wait
