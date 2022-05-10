import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a file descriptor is ready

# Return value: three lists of objects that are ready

# select() is a useful tool for multiplexing input and output.
# It can be used to wait for a timeout period for a blocking operation to complete.
# It can be used to wait for a file descriptor to become ready for some class of I/O operation (e.g. input possible).
# It can be used to multiplex many file descriptors onto a single file descriptor, so that a single thread can manage multiple communications channels.

# select() can be used to implement a timeout on blocking I/O operations.
# If the timeout period expires before the operation is complete, select() returns three empty lists.
# If the operation is completed before the timeout period expires, select() returns three lists containing only those
