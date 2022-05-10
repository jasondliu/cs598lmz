import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until a monitored file descriptor becomes ready; if zero, return immediately even if no file descriptors are ready; if given and not zero, block for that many seconds
#
# Return value:
#
# Three lists are returned, one for each of the three lists of monitored file descriptors. Each contains the subset of the corresponding file descriptors that are ready.
#
# select.select() may modify the lists it receives as arguments, so you should pass them in each time you call the function.
#
# select.select() is a useful way to multiplex input from multiple sources. For example, if you want to wait for input from both stdin and a socket, use select() to wait until input is ready from either source, then read from the ready source.
#
# select.select() is also
