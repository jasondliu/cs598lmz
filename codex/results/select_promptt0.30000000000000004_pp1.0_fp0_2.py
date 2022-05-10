import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# select() returns three lists of file descriptors: those that are ready for reading, those that are ready for writing, and those that have raised exceptions.
# If a file descriptor appears in any of the lists, it means that it is ready for the corresponding I/O operation.
# If a file descriptor does not appear in any of the lists, it means that it is not ready for any of the corresponding I/O operations.
# If the timeout is reached without any file descriptors becoming ready, three empty lists are returned.

# select() is available on Unix and Windows.
# On Unix, it supports file descriptors, as well as sockets and pipes.
# On Windows, it supports sockets, pipes, and devices.

# select() is a useful tool for performing
