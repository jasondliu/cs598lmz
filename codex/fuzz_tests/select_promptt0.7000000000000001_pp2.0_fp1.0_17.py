import select
# Test select.select()
# http://docs.python.org/2/library/select.html

# select(rlist[, wlist[, xlist[, timeout]]])
# Wait until one or more file descriptors are ready for some kind of I/O. The first three arguments are sequences of file descriptors to be waited for: rlist, wlist, xlist.
# The optional timeout argument specifies a time-out as a floating point number in seconds. When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
# A time-out value of zero specifies a poll and never blocks.
# The return value is a triple of lists of objects that are ready. The first list contains those descriptors with input available, the second those with output room, and the third those that have raised exceptions.
# This function is only available on Unix.

# The fdlist tuple is updated to include only the file descriptors that are ready.
# This method is most commonly used to multiplex input from several sockets. Note that the select function does not provide any way to perform a timeout in the accept method of a socket object, so if you need to enforce a
