import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# 
# Monitor sockets specified in rlist, wlist, xlist.
# If a socket is ready for reading, it will be added to rlist.
# If a socket is ready for writing, it will be added to wlist.
# If a socket is ready for an error condition to be checked, it will be added to xlist.
#
# The optional timeout argument specifies a timeout in seconds; it may be a floating point number to specify fractions of seconds.
# If timeout is omitted the call will never time out.
#
# Return value is a triple of lists of objects that are ready: (rlist, wlist, xlist)
#
# If the time-out is reached without any file descriptors becoming ready, three empty lists are returned.
#
#
# select.select([r],[w],[x],timeout)
#
# r, w, x are lists of sockets to be checked
# timeout is the time to wait for a socket to become ready
#
# select.select() returns three lists of sockets that are ready for reading,
