import select
# Test select.select()
# select.select([inputs], [], [], timeout)
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# select.select() returns three lists of objects that are ready:
# rlist: those sockets ready for reading
# wlist: those sockets ready for writing
# xlist: those sockets with exceptions

# select.select() will block until at least one file descriptor is ready.
# A file descriptor is considered ready if it is possible to perform the corresponding I/O operation (e.g. read()) without blocking.

# select.select() supports sockets, pipes and devices.
# select.select() does not support file objects on Windows.
# select.select() does not support file objects on Windows.
# select.select() does not support file objects on Windows.
# select.select() does not support file objects on Windows.
# select.select() does not support
