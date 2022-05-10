import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: a time-out as a float in seconds
#
# Return value: three lists of objects that are ready
#
# The select() function monitors all the I/O channels you are interested in, and returns three lists of objects:
#
# those that are ready for reading (“rlist”),
# those that are ready for writing (“wlist”), and
# those that have an exceptional condition (“xlist”).
#
# The objects in the lists are file objects corresponding to the channels monitored by select().
#
# The optional timeout argument specifies a time-out as a floating point number in seconds. When the timeout argument is omitted the function blocks until at least one file descriptor is ready. A time-out value of zero specifies a poll and never blocks.
#
# A
