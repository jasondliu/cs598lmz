import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor is ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() can be used as an efficient way to multiplex input/output over a number of sockets or other file objects.
# It can also be used to wait until a file is ready for some kind of I/O operation.

# The following example shows how to use select() to monitor a number of sockets and connections for data available to read.
# The sockets and connections are added to the rlist, and the select() call blocks until one or more of the sockets or connections are ready.

# The example also shows how to use select() to monitor a number of sockets and connections for space available to write.
# The sockets and connections are added to the wlist,
