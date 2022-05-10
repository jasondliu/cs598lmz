import select
# Test select.select()
# select.select() blocks until one of the sockets is ready for some kind of I/O
# select.select() returns three lists of sockets which are ready for I/O.
# The first list contains sockets which are ready for reading, the second list
# contains sockets which are ready for writing, and the third list contains
# sockets which have an error condition.
#
# The optional timeout parameter specifies a time-out as a floating point
# number in seconds. When the timeout argument is omitted the function blocks
# until at least one socket is ready. A time-out value of zero specifies a poll
# and never blocks.
#
# The return value is a triple of lists of objects that are ready:
# (rlist, wlist, xlist)
#
# The first three arguments to select() are sequences of objects to be checked
# for readiness. The first is a sequence of objects to be checked for read
# availability, the second is a sequence of objects to be checked for write
# availability, and the last is objects to be checked for “exceptional conditions”.
#
# If the timeout is omitted or None, the call
