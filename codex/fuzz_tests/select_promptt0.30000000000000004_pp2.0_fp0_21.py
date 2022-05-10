import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified or None, block until at least one file descriptor is ready; otherwise, block for at least timeout seconds (or until a file descriptor is ready, if timeout is a floating point number)
# Return value: three lists of objects that are ready

# The select() function can be used to wait until a file descriptor becomes ready for some class of I/O operation (e.g. input possible). The first three arguments are sequences of file descriptors to be waited for: rlist – wait until ready for reading, wlist – wait until ready for writing, xlist – wait for an “exceptional condition” (see the manual page for what your system considers such a condition). The optional fourth argument specifies a timeout in seconds; it may be a floating point number to specify fractions of seconds. If all three arguments are omitted, select() returns an empty
