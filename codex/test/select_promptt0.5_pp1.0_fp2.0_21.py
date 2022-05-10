import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# select.select() returns three lists of objects that are ready: subsets of the first three arguments. When the timeout argument is omitted the function blocks until at least one file descriptor is ready. A zero timeout causes the function to return immediately, even if no file descriptors are ready; this can be used to poll().

# A file descriptor is considered ready if it is possible to perform the corresponding I/O operation (e.g., read()) without blocking.

# select.select() can be interrupted by a signal (see the signal module). On some systems, you can use the signal module to set a signal handler that will be called as soon as a signal is received; the handler will interrupt the select.select() call, and the call will return three empty lists.

# On other systems, the signal handler will only be called after the select.select() call returns;
