import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not given, will block until a monitored file descriptor becomes ready

# select() returns three lists of file descriptors: those that are ready for reading, those that are ready for writing, and those that have an exceptional condition pending.

# If a file descriptor appears in all three lists, it is always returned only once.

# If the timeout is reached before anything interesting happens, select() returns three empty lists.

# If an error occurs, select() raises an exception.

# If the select() call is interrupted by a signal (or the timeout expires), three empty lists are returned.

# select() always returns the lists in the same order as the arguments were given.

# select() does not modify the lists you pass in.

# select() does not return until the requested operation is possible or the timeout occurs.

# select
