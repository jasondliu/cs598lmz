import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not specified, wait forever
#
# The return value is a triple of lists of objects that are ready:
# (subset of rlist, subset of wlist, subset of xlist)
#
# If the time-out is reached without a file descriptor becoming ready, three empty lists are returned.
#
# select() may modify the lists it is given as arguments, so you should pass them in each time you call select().
#
# select() does not necessarily return in the order in which the file descriptors become ready.
#
# select() is not a very good interface for most applications, because it does not provide a way to find out why a file descriptor became ready.
#
# select() is not available on all systems.
#
# select() is not available on all systems.
#
# select
