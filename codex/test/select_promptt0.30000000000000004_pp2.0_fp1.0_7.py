import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified (or if specified as None), block until an event occurs

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output.
# It can be used to wait for a socket to become readable, writable or have pending errors.
# It can also be used to wait for a file descriptor to become readable or writable.
# The select() function is available on Unix and on Windows.

# The select() function takes three lists of sockets (or file descriptors) as arguments.
# The first list contains sockets that will be checked for readability,
# the second contains sockets that will be checked for writability,
# and the third contains sockets that will be checked for errors.
# The function returns a list of
