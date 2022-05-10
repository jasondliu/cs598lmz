import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready
#
# Return value: three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready
#
# select.select() can be used as an efficient way to wait until any of multiple file descriptors is ready for some kind of I/O.
#
# The following example uses select() to implement a simple, single-threaded web server.
#
# The server uses select() to handle multiple connections at the same time.
#
# The server handles one connection at a time, but it could easily be modified to handle multiple connections simultaneously.
#
# The server handles GET requests only.
#
# The server is single-threaded, so it can handle only one request at a time.
#
#
