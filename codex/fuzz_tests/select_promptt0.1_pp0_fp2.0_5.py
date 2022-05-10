import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input and output.
# It can be used to wait for input on many file descriptors at once.
# It can also be used to implement a timeout while waiting for input.

# select.select() takes three lists of objects:
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# The return value is a tuple of three lists of objects that are ready:
# (rlist, wlist, xlist)

# The select module also defines some constants that can be used as the third argument to select()
# to specify the type of event
