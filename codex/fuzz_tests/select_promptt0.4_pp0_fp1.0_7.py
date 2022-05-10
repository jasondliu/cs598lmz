import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not given, block until a monitored file descriptor becomes ready; if zero, return three empty lists; if positive, block at most that many seconds

# The return value is a tuple of three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready

# select.error: exception raised in the case of an error
# select.select() will raise this exception if any of the file descriptors is invalid.

# select.poll()
# select.poll() is a variant useful for programs that need to handle a large number of file descriptors. It uses a different underlying mechanism so it can handle an arbitrary number of descriptors, but it has restrictions on the file descriptors that can be used.

# select.poll() returns a poll object, which supports registering and unregistering file descriptors, and then
