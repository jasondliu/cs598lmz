import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select() can be used as an efficient way to multiplex input/output over a number of sockets or other file-like objects.
# It can also be used to monitor a single file descriptor.

# select() can also be used to monitor multiple file descriptors, waiting until one or more of the file descriptors become “ready” for some class of I/O operation (e.g. input possible).
# A subsequent read or write will not block, and will return data that is available (or return an error if there is no data available on the selected file descriptor).

# select() is also useful for implementing timeout mechanisms.
# The select() function blocks until
