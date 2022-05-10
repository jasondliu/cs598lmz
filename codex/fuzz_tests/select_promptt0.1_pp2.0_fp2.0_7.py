import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input/output access to many file descriptors in a program with many threads.
# It is the basis for the select() function available in some higher-level languages.

# select.select() is also useful for handling sockets.
# For example, a server that needs to handle multiple connections at once can use select.select() to determine when a client socket is ready to read or write data.

# select.select() is also useful for handling sockets.
# For example, a server that needs to handle multiple connections at once can use select.select() to determine when a client socket is ready to read or write data.

