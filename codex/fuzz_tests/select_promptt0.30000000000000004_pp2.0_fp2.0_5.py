import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified or None, select() can block indefinitely

# select.select() returns three lists of objects that are ready:
# rlist: objects ready for reading
# wlist: objects ready for writing
# xlist: objects with “exceptional conditions”

# If the time limit is reached with no file descriptors ready, three empty lists are returned.

# If select() is interrupted by a signal (or the timeout expires, or if another error occurs),
# three empty lists are returned.

# select.select() can be used as a sleep() function if all file descriptors are specified as empty lists.

# select.select() can be used to monitor multiple file descriptors, waiting until one or more of the file descriptors
# become “ready” for some class of I/O operation (
