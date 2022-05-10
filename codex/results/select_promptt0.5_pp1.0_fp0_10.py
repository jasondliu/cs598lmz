import select
# Test select.select()
#
# Returns three lists of objects that are ready for reading, writing, and
# erroring, respectively.
#
# This function is a higher-level wrapper around the epoll() and poll()
# functions.
#
# The first three arguments are sequences of objects to be waited for:
# rlist -- wait until ready for reading
# wlist -- wait until ready for writing
# xlist -- wait for an ``exceptional condition''
# If only one kind of condition is required, pass [] for the other lists.
# A file descriptor is either a socket or file object, or a small integer
# gotten from a fileno() method call on one of those.
#
# The optional fourth argument specifies a timeout in seconds; it may be
# a floating point number to specify fractions of seconds.  If it is absent
# or None, the call will never time out.
#
# The return value is a tuple of three lists of objects that are ready:
# (rlist, wlist, xlist)
#
# A file descriptor is considered ready if it is possible to perform the
# corresponding I/O operation (e.g
