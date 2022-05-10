import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# If the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

# If select() is interrupted by a signal (or the time-out expires, or one of the file descriptors being monitored by a select() call is closed), it returns an empty list.

# select() may modify the timeout argument.

# select() should not be interrupted by a signal (other than SIGALRM) unless the SA_RESTART flag was used to change the signal disposition for the interrupting signal.

# select() should not be used as a sleep function.

# select() should not be used to implement a busy-wait loop.

# select() should not be used to implement a wait loop.

# select() should not be used to implement
