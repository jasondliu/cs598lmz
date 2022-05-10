import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not supplied, block until a monitored file descriptor becomes ready
# Return value: three lists of objects that are ready
# (a) rlist: those fds that are ready for reading
# (b) wlist: those fds that are ready for writing
# (c) xlist: those fds that have an exception (e.g., out-of-band data)
# If the timeout is reached with no file descriptors ready, three empty lists are returned.

# select.select() is used to monitor multiple file descriptors, waiting until one or more of the file descriptors become “ready” for some class of I/O operation (e.g., input possible). The first three arguments are sequences of file descriptors to be waited for: rlist, wlist, xlist — which can be modified on return (see
