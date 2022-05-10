import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until a monitored file descriptor becomes ready; if zero, do not block at all; otherwise, block for at most timeout seconds

# select.poll()
# select.poll() -> poll object
# Create a new polling object.

# select.poll.poll(timeout=None)
# Poll the set of registered fds.
# timeout specifies a maximum interval to wait, in milliseconds. It may be:
# None: wait forever
# 0: don’t wait at all, and return immediately
# positive integer: wait up to timeout milliseconds
# The return value is a list containing any descriptors that have events or errors to report.

# select.poll.register(fd, eventmask=POLLIN|POLLPRI|POLLOUT)
# Register a file descriptor with the polling object.

