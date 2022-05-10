import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a file descriptor is ready
#
# Returns three lists of file descriptors: rlist, wlist, xlist
#
# select() will return three lists of file descriptors:
#
# rlist: those sockets ready for reading
# wlist: those sockets ready for writing
# xlist: those sockets with exceptions
#
# If the timeout is reached before anything interesting happens, three empty lists are returned.
#
# If select() is interrupted by a signal (or the timeout expires), three empty lists are returned.
#
# If select() is interrupted by a signal (or the timeout expires), it will return immediately with three empty lists.
#
# If select() is interrupted by a signal (or the timeout expires), it will return immediately with three empty lists.
#

