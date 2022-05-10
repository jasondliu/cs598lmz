import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# select.select() returns three lists of objects that are ready:
# rlist: those sockets ready for reading
# wlist: those sockets ready for writing
# xlist: those sockets with exceptions

# select.select() can be interrupted by a signal (this is a limitation with the underlying select() system call).
# In order to restart the select() system call, you need to set the signal handler for the signal to the original
# signal handler and call select() again.

# select.select() can also be interrupted by a signal (this is a limitation with the underlying select() system call).
# In order to restart the select() system call, you need to set the signal handler for the signal to the original
# signal handler and call select() again.

#
