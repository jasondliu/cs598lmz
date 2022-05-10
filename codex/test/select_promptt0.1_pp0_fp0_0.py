import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments
# If the time out is reached without a file descriptor becoming ready, three empty lists are returned.

# select.select() is a useful way to multiplex input from multiple sockets.
# It can also be used to multiplex input from a single socket.
# For example, if you want to wait for input from stdin and a socket, you can do this:

# rlist, wlist, xlist = select.select([sys.stdin, sock], [], [])
# if sys.stdin in rlist:
#     data = sys.stdin.readline()
#     ...
# if sock in rlist:
#     data = sock
