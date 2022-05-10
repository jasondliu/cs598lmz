import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sockets.

# Example:
# rlist, wlist, xlist = select.select([conn1, conn2], [], [])
# if conn1 in rlist:
#     data = conn1.recv(1024)
#     ...
# if conn2 in rlist:
#     data = conn2.recv(1024)
#     ...

# select.select() is also useful for waiting until a file descriptor is ready for reading/writing, without actually reading/writing any data.

# Example:
# rlist, wlist, xlist =
