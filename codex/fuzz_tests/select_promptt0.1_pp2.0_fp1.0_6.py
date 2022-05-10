import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select() is a useful tool for multiplexing input/output over a number of sockets or other file objects.
# It can be used to implement client/server applications, for example, where one or more clients are connected to a server and
# where the server wants to attend to each client in turn to perform some application-level processing.
# The server would use select() to determine when a client socket is ready to perform a read or write operation.

# select() can also be used to implement a timeout on I/O operations,
# by passing a timeout parameter to select() and then testing for the returned lists being empty.

# select() is also useful for handling inputs
