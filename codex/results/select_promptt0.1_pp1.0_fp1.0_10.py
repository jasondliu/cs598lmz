import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input and output
# across multiple sockets and/or files.

# select.select() is also useful for implementing timeout functionality
# in a program.

# select.select() can be used to monitor multiple file descriptors,
# waiting until one or more of the file descriptors become “ready” for some class of I/O operation
# (e.g. input possible).

# select.select() takes three lists of file descriptors:
# the first contains the descriptors to be checked for being ready to read,
# the second contains the descriptors to be checked for being ready to write,
# and the third contains the descriptors to be checked for error conditions.

# The return value is a
