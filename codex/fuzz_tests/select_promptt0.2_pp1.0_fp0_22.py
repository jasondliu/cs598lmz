import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until a monitored file descriptor becomes ready; if zero, return immediately even if no file descriptors are ready; if timeout is a float, it specifies a timeout in seconds (to microsecond resolution)
#
# Return value: three lists of objects that are ready: subsets of the first three arguments
#
# select.select() can be interrupted by a signal (see the signal module)
#
# select.select() can also be used with pipes and sockets.
#
# select.select() is a useful way to multiplex input/output over sockets and pipes.
#
# select.select() is not available on all platforms — it’s implemented only on Unix and Windows.
#
# select.select() is a useful way to multiplex input/output over sockets and pipes.
#

