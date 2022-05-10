import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not supplied, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select.poll()
# select.poll() -> poll object
# Create a polling object.

# This supports registering and unregistering file descriptors, and then polling them for I/O events.

# The poll object supports registering file descriptors to be polled for a specific type of I/O event, as well as polling for I/O events currently waiting to be processed.

# select.poll.register(fd[, eventmask])
# Register a file descriptor with the polling object.

# The fd argument is the file descriptor of the file to be monitored, and the eventmask argument is an optional bitmask describing the type of events to check for.

# The eventmask argument can
