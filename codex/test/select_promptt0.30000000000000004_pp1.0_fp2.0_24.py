import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready
#
# Return value: three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready
#
# select.select() can be used as an efficient way to wait until a socket is ready for reading or writing
#
# select.select() can also be used to monitor multiple sockets at once, in effect creating a simple “polling” interface
#
# select.select() can also be used with pipes and other devices
#
# select.select() can be interrupted by a signal (such as SIGINT or SIGALRM)
#
# select.select() can be used to implement a timeout for blocking socket operations
#
# select.select() can be used with a timeout of zero to poll the set
