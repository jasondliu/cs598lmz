import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.select() can be used to monitor multiple sockets at the same time,
# waiting until one or more of the sockets are ready for some kind of I/O.
# The first argument is a list of sockets to be checked for readiness for reading;
# the second is a list of sockets to be checked for readiness for writing;
# the third is a list of sockets to be checked for errors;
# and the fourth is the timeout in seconds.

# The return value is a tuple of three lists of sockets corresponding to the first three arguments;
# each list contains those sockets that are ready for the corresponding operation.

# For example, if you want to wait until a socket is ready for reading,
# do select.select([sock], [], [], []) and if
