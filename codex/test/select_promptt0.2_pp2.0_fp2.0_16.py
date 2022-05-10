import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not supplied, block until a monitored file descriptor becomes ready; if supplied as a float with a nonzero value, block until the timeout has elapsed or a monitored file descriptor becomes ready; if supplied as None, block until a monitored file descriptor becomes ready or the call is interrupted by a signal
# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.poll()
# poll() is a more efficient way to wait for multiple file descriptors to become ready for I/O.

# select.epoll()
# epoll() is a variant of poll() that scales well to large numbers of watched file descriptors.

# select.kqueue()
# kqueue() is a variant of poll() available on BSD-derived systems.

# select.kevent()
# kevent() is a variant
