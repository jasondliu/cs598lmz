import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# select() returns three lists of file descriptors: those that are ready for reading, those that are ready for writing, and those that have raised exceptions.
# If a file descriptor appears in both the readable and writable lists, it means that it is possible to read from it without blocking, and to write to it without blocking.
# If a file descriptor appears in both the readable and the exceptional lists, it means that an out-of-band message has arrived on the socket, and that the next recv() will not block.
# If a file descriptor appears in both the writable and the exceptional lists, it means that the socket is broken and that the next send() will not block.

# The file descriptor sets are modified in place by select() to indicate which descriptors are ready.
