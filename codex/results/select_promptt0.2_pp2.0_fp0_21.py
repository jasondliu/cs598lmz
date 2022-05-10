import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not supplied, block until a monitored file descriptor becomes ready; if supplied as a float, it specifies a timeout in seconds; as a tuple of two floats, the first is a timeout in seconds and the second is a timeout in microseconds

# Return three lists of “ready” file descriptors.

# The first list contains those descriptors that are readable, the second contains writable descriptors, and the third contains those that have an “exceptional condition” (for example, out-of-band data).

# The select() function is a direct interface to the underlying operating system implementation. It does not modify the file descriptor sets; they may be reused across calls to select() if desired.

# The return value is a tuple of three lists of file descriptors.

# The first list contains the subset of the monitored file
