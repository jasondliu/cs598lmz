import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, wait forever

# Return value: three lists of objects that are ready

# select.poll()
# select.poll() is a more advanced version of select()
# It returns a poll object, which supports registering and unregistering file descriptors, and then polling them for I/O events.
# The poll object has a register() method which takes a file descriptor and an event mask as arguments.
# The event mask is a bitmask of the events to be checked for the file descriptor.
# The event mask can be constructed using the constants POLLIN, POLLOUT, and POLLERR.
# The poll object has a poll() method which takes a timeout argument in milliseconds.
# It returns a list of (fd, event) tuples, where fd is the file descriptor, and event is an event
