import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])

# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# timeout is in seconds; it may be a floating point number to specify fractions of seconds.
# If timeout is omitted or None, the call will never timeout.

# Return value: three lists of objects that are ready: subsets of the first three arguments.

# When the specified condition is true for any of the objects, select() returns immediately.
# Otherwise, it waits until the specified timeout expires and all conditions are true.
# A libc select() based implementation is provided, but it is not warranted efficient.
# Do not rely on select() to provide accurate sub-second timeouts.
# Also note that if the timeout is zero, then select() can return earlier than stated.

# select() may modify any of the lists it is given as arguments.
# Use select.select() to monitor multiple file descriptors.

#
