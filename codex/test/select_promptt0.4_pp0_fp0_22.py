import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file becomes ready

# select.poll()
# select.poll() is a class that can be used to monitor multiple file descriptors.
# poll() return a list of tuples containing the file descriptor and event mask.
# The event mask is a bit mask of various events.
# The constants for the event mask are defined in the select module.
# The values have the same meaning as the corresponding arguments to select().
# POLLIN: There is data to read
# POLLPRI: There is urgent data to read (e.g., out-of-band data on TCP socket; pseudoterminal master in packet mode has seen state change in slave)
# POLLOUT: Writing now will not block
# POLLERR: Error condition (only returned in revents; ignored in events)
