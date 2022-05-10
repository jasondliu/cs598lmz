import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input/output over a set of file descriptors.
# It can be used to implement a simple network server.

# The following example shows how to use select() to handle three inputs at once.

# The first input is a list of connections to be monitored for input.
# The second input is a list of connections to be monitored for output.
# The third input is a list of connections to be monitored for exceptions.
# The example uses a timeout of 5 seconds.

# The example also shows how to use select() to monitor a file for input.

# The example uses a timeout of 5 seconds.
