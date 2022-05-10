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
# select() can be used as an efficient way to multiplex input/output over a set of file descriptors.
#
# The following example shows how to use select() to multiplex two sockets and standard input (sys.stdin).
#
# The example is a simple echo server that listens on port 5000 and echoes back whatever it receives.
#
# The server uses select() to handle multiple connections simultaneously in a non-blocking manner.
#
# The server starts by creating a non-blocking TCP/IP socket and configuring it to listen on an address.
#
# It then enters a loop where it calls
