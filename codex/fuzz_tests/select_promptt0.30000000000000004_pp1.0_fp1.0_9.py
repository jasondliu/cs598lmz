import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, wait forever

# Return value: three lists of objects that are ready
# rlist: objects in rlist that are ready for reading
# wlist: objects in wlist that are ready for writing
# xlist: objects in xlist that have an “exceptional condition”

# The select() function is a direct interface to the underlying operating system implementation.
# It does not modify the objects, so they can be used with any select() implementation, not just select().

# The select() function supports file objects, sockets, pipes, and devices.

# The following example shows how to use select() to monitor a pair of sockets for data to read.
# If there is data to read, it will be read and echoed back to the client.
# If there is no data to read, the program waits
