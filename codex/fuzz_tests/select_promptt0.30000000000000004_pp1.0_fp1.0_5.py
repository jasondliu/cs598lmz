import select
# Test select.select()

# select.select() can monitor multiple file descriptors, waiting until one or more of the file descriptors become "ready" for some class of I/O operation (e.g. input possible).
# select.select() is a straightforward way to implement asynchronous I/O in Python.
# select.select() can be used with any file descriptor, not just sockets.
# select.select() can be used with pipes, but not with files.

# select.select() takes three lists of file descriptors:
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)

# select.select() returns three lists of file descriptors:
# rlist: those file descriptors that are ready for reading
# wlist: those file descriptors that are ready for writing
# xlist: those file descriptors that have an "exceptional condition"

# select.select() can be told to wait only a specified amount of time for the file descriptors to become ready.
# If the timeout period value
