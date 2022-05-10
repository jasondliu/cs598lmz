import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# select.select() returns three lists of objects that are ready: subsets of the first three arguments.
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A negative or None timeout means to block indefinitely.

# select.select() can be interrupted by a signal (see the signal module) and in such cases returns three empty lists.
# (On some systems select.select() may also return an empty list when a file descriptor is ready but the call is interrupted by a signal.)

# select.select() is intended for polling and not for waiting for I/O completion.
# If you are interested in waiting for I/O completion, see the Unix manual page for select(2) and the BaseServer class.

# select
