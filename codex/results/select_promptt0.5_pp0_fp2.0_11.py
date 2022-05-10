import select
# Test select.select
#
# select.select(rlist, wlist, xlist[, timeout])
#
# If the optional timeout argument is present and not None,
# it should be a floating point number specifying a timeout
# for the operation in seconds (or fractions thereof).
# If the timeout argument is absent or None, the call will
# never time out.
#
# select.select() return three lists of objects that are ready:
# rlist: objects ready for reading
# wlist: objects ready for writing
# xlist: objects with exceptions
#
# The return value is a tuple of three lists of objects that are ready:
# rlist, wlist, xlist = select.select(rlist, wlist, xlist[, timeout])
#
# The select.select() method is a straightforward interface
# to the Unix select() system call. The first three arguments
# are sequences of ‘waitable objects’: either integers
# representing file descriptors or objects with a parameterless
# method named fileno() returning such an integer:
#
# These are followed by an optional timeout in seconds;
# if the timeout is
