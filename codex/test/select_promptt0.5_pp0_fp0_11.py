import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# wait until one or more file descriptors are ready for some kind of I/O.
# The first three arguments are sequences of file descriptors to be waited for:
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
#
# If only one kind of condition is required, pass [] for the other lists.
# A file descriptor is either a socket or file object, or a small integer
# gotten from a fileno() method call on one of those.
#
# The optional 4th argument specifies a timeout in seconds; it may be a
# floating point number to specify fractions of seconds. If it is absent or
# None, the call will never time out.
#
# The return value is a triple of lists of objects that are ready:
#   sublist of rlist: objects ready for reading
#   sublist of wlist: objects ready for writing
#   sub
