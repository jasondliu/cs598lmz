import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready
# rlist: objects in rlist that are ready for reading
# wlist: objects in wlist that are ready for writing
# xlist: objects in xlist that have an “exceptional condition”

# select.error: exception raised in case of an error

# select.select() is a blocking call.
# If the timeout is zero, then select() will return immediately,
# without waiting for any file descriptors to become ready.

# select.select() can be interrupted by a signal (such as SIGALRM).
# In that case, three empty lists are returned.

# select.select() can also be interrupted by a signal
# (such as SIGINT or SIG
