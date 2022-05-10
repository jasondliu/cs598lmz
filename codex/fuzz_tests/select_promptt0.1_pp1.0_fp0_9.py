import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready
#
# Return value: three lists of objects that are ready
#
# select.select() is a blocking call.
#
# select.select() is a portable way to wait until a file descriptor is ready for some kind of I/O.
#
# select.select() supports timeout and so is good for implementing network clients.
#
# select.select() can be interrupted by a signal (this is usually not possible with the underlying system call).
#
# select.select() can be used with pipes, FIFOs and files.
#
# select.select() can be used with sockets.
#
# select.select() can be used with devices.
#
# select.select() can be used with ttys.
#
