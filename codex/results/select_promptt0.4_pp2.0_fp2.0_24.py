import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an ``exceptional condition'' (see the manual page)
# timeout: if not supplied (or None), block until a file descriptor is ready;
#          otherwise, timeout should be a float, and the call will return
#          three lists after that number of seconds has passed, even if
#          no file descriptors are ready.

# Return value: three lists of objects that are ready: subsets of the
# first three arguments.

# The first three arguments are sequences of file descriptors to be waited for:
# rlist -- wait until ready for reading
# wlist -- wait until ready for writing
# xlist -- wait for an ``exceptional condition''
# The optional fourth argument specifies a timeout in seconds; it may be
# a floating point number to specify fractions of seconds.  If it is absent
# or None, the call will never time out.

# The return value is a tuple of three lists corresponding to the first three
