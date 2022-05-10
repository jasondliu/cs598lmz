import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select.select() will always return three lists, even if they are empty.

# select.select() can be interrupted by a signal (this is a limitation of the underlying select() system call).

# select.select() can also be interrupted by a signal if the signal handler raises an exception (this is a limitation of the underlying select() system call).

# select.select() can also be interrupted by a signal if the signal handler calls a function that calls select.select().

# select.select() can also be interrupted by a signal if the signal handler calls a function that calls a function that calls select.select().

# select.select() can also be interrupted by a signal if the signal handler calls a
