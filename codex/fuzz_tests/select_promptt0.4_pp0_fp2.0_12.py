import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not supplied, block until a monitored file descriptor becomes ready;
# if supplied and is a positive integer, block until a file descriptor becomes ready or the timeout has elapsed;
# if supplied and is 0, do not block at all, but return immediately even if no file descriptors are ready;
# if supplied and is negative, block indefinitely.

# select() returns three lists of file descriptors: those that are ready for reading, those that are ready for writing, and those that have an error condition pending.
# select() will never return more than one of the three lists empty.

# select() is useful if you have multiple sockets to monitor and don’t want to use a thread for each one.
# select() is also useful if you want to implement a timeout on I/O operations, as you can ask it to return after a specified number
