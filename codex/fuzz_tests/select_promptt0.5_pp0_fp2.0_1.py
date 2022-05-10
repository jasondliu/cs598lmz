import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist, wlist, xlist -- lists of selectables to monitor
# timeout -- maximum time to wait in seconds;
# if omitted (or None), will block until at least one file descriptor is ready
# returns three lists of selectables: those that are ready for reading, writing, and exceptional conditions
# When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A negative or None timeout means to wait indefinitely.
#
# select.select() is a useful tool for monitoring multiple file descriptors, but suffers from race conditions.
# When a file descriptor is ready for a given I/O operation, the kernel will wake up the process,
# but it will not perform the operation itself.
# There is no way to know whether the file descriptor will still be ready by the time the process wakes up.
# If the file descriptor is still ready, the operation can be performed.
# If it is no longer ready, the select call must be repeated.
#
# If a file descriptor is ready for reading, select does not guarantee that a subsequent read
