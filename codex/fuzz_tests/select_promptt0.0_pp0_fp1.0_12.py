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

# The following example shows how to use select() to handle three sockets while at the same time continuing to
# run a time consuming task in parallel.

# The time consuming task is simulated by the function time.sleep().

# The select() function is called with three lists of sockets:
# the first contains sockets with data available to read,
# the second sockets ready for writing,
# and the last sockets with an exceptional condition.
# The timeout argument specifies how long to wait for a response,
