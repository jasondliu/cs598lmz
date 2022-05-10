import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Returns three lists of file descriptors: subsets of the first three arguments
# The first list contains those descriptors which are ready for reading,
# the second contains those ready for writing,
# and the third those that have an exceptional condition pending.

# select.select() is a useful way to multiplex input/output access to many file descriptors in a program.
# It is the basis for many of the higher-level I/O functions in the Python standard library.

# select.select() is available on Unix and Windows.
# On Unix, it supports file descriptors, as well as sockets.
# On Windows, it supports sockets, named pipes, and console input.

# select.select() is a blocking call.
# If you want
