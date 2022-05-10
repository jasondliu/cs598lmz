import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return immediately even if no file descriptors are ready; if given and not zero, it specifies a timeout in seconds (float) and the function will return three lists after that time even if no file descriptors are ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select() can be interrupted by a signal (see the signal module) and in that case returns three empty lists

# select() should not be used if you need to be able to cancel the operation from another thread. Use poll() or epoll() instead.

# select() supports file descriptors, not file objects.

# select() only works on sockets, or other file-like objects as long as they have a fileno() method that returns a
