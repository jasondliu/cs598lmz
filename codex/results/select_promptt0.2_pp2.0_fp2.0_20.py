import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready
# rlist: objects in rlist that are ready for reading
# wlist: objects in wlist that are ready for writing
# xlist: objects in xlist that have an “exceptional condition”

# If the timeout is reached without a file descriptor becoming ready, three empty lists are returned.

# select.select() is a useful way to multiplex input from multiple sockets.
# It can also be used to multiplex input from a single socket.
# For example, if you want to wait for data to arrive on a socket,
# or for a user to type something on standard input,
# you can use select() to wait for either event to occur.

# select.select()
