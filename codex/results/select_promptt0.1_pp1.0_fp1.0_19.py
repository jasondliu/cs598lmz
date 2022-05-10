import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input/output over a number of sockets or other file-like objects.

# select.select() can be used to monitor a number of sockets for activity, and if a socket is ready, perform a send or receive operation on it.

# select.select() can also be used to monitor a single socket for availability of data to read.

# select.select() can be used to monitor a single socket for the ability to write data.

# select.select() can be used to monitor a single socket for an “exceptional condition”.

# select.select() can be used to monitor a single socket for the ability to read or write
