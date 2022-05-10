import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready
# rlist: objects in rlist that are ready for reading
# wlist: objects in wlist that are ready for writing
# xlist: objects in xlist that have an “exceptional condition”

# select.select() can be used to monitor multiple file descriptors, waiting until one or more of the file descriptors become “ready” for some class of I/O operation (e.g., input possible). The first three arguments are sequences of file descriptors to be waited for: rlist — wait until ready for reading, wlist — wait until ready for writing, xlist — wait for an “exceptional condition” (see the manual page for what your system considers such a condition). The
