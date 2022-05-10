import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return immediately even if no file descriptors are ready; if given and not zero, block for at most that many seconds
# Return value: three lists of file descriptors: those that are ready for reading, those that are ready for writing, and those that have an “exceptional condition” (see the manual page for what your system considers such a condition)

# select.select() is a blocking call, and will block until the timeout expires or a monitored file descriptor becomes ready.
# select.select() will never “miss” an event (in the sense that if a monitored file descriptor becomes ready, then select.select() will always return it in one of the lists), but it can “lose” an event (in the sense that if a file descriptor
