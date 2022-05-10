import select
# Test select.select()
#
# The select.select() method is a blocking call that takes three arguments:
#
#     select.select(rlist, wlist, xlist[, timeout])
#
# The rlist is a list of sockets that are ready for reading.
# The wlist is a list of sockets that are ready for writing.
# The xlist is a list of sockets that have raised exceptions.
# The timeout is an optional integer that specifies the number of seconds to wait for an event to occur.
# If timeout is None, then select() blocks until at least one file descriptor is ready.
#
# The return value is a tuple of three lists.
# The first list contains the file descriptors that are ready for reading.
# The second list contains the file descriptors that are ready for writing.
# The third list contains the file descriptors that have raised exceptions.
#
# If the timeout expires before any events occur, then the three lists are all empty.
#
# The select.select() method is typically used with sockets.
# A socket can be put in non-blocking mode by setting the socket’s blocking flag to False.

