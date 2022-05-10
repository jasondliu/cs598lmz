import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output, for example, when you have a user interface in one thread and a server in another.

# select.select() can also be used to monitor multiple sockets at the same time.

# select.select() can be used to monitor a file descriptor and wait until it is ready for some class of I/O operation.

# select.select() can be used to monitor a file descriptor and wait until it is ready for reading, writing, or an “exceptional condition”.

# select.select() can be used to monitor a file descriptor and wait until it is ready for reading, writing,
