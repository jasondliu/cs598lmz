import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; else a float, the maximum time to block in seconds (or until a signal arrives, on Unix); zero for non-blocking mode; negative or None for blocking mode
# Return value: three lists of objects that are ready

# select.poll()
# select.poll() -> poll object
# Create a new polling object.
# This supports registering and unregistering file descriptors, and then polling them for I/O events.
# The following event flags are defined:
# POLLIN: There is data to read
# POLLPRI: There is urgent data to read
# POLLOUT: Writing now will not block
# POLLERR: Error condition
# POLLHUP: Hung up
# POLLNVAL: Invalid request: fd not open
