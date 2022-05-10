import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
#
# Return value:
#
# Three lists are returned, one for each channel.
# Each contains the subset of the corresponding channel that is ready.
#
# If the timeout is omitted, it defaults to -1, which means to block until at least one file descriptor is ready.
# If the timeout is zero, the call returns three empty lists immediately.
#
# If the timeout is positive, it specifies a maximum wait time in seconds.
# The return value is a triple of lists of objects that are ready:
#
# rlist: objects ready for reading
# wlist: objects ready for writing
# xlist: objects with exceptions
#
# If the timeout is reached without a file descriptor becoming ready, three empty lists are returned.
#
# select.select() can be interrupted by a signal (see the signal
