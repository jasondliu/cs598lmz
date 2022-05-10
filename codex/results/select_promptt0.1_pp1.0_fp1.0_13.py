import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input and output.
# It is the basis for the select() method of socket objects.

# select.select() can also be used to monitor multiple file descriptors, waiting until one or more of the file descriptors become “ready” for some class of I/O operation (e.g. input possible).
# The first three arguments to select() are sequences of file descriptors to be waited for: rlist — wait until ready for reading, wlist — wait until ready for writing, xlist — wait for an “exceptional condition” (see the manual page for what your system considers such a condition).
# The optional fourth argument specifies a timeout in seconds; it may be a floating point number to specify fractions of seconds.
