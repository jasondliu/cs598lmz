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

# select.select() takes three lists of sockets/files as arguments.
# The first list contains the sockets/files to be checked for being
# ready for reading. The second list contains the sockets/files to
# be checked for being ready for writing. The third list contains
# the sockets/files to be checked for errors.

# The return value is a tuple of three lists. The first list contains
# the sockets/files that are ready for reading. The second list
# contains the sockets/files that are ready for writing. The third
# list contains the sockets
