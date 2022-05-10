import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
#
# timeout: how long to wait, in seconds
#
# The return value is a tuple of three lists corresponding to the first three arguments; each contains the subset of the corresponding file objects that are ready.
#
# A file object is ready when a new input arrives that can be read immediately, or when an output buffer has room again.
#
# An empty list is returned if the timeout period value has been reached and no file descriptors are ready.
#
# If all three lists are empty, the timeout period has elapsed, and the call has timed out.
#
# (The documentation says that an empty list may be returned if the timeout period is zero, but I have never seen this happen.)

# The select() function is a direct interface to the underlying operating system implementation.
# It examines the I/O readiness of the file objects
