import select
# Test select.select
# https://docs.python.org/2/library/select.html
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual for more info)
#
# All three arguments are optional, and default to three empty lists.
#
# select.select() returns three lists of objects which are ready:
# rlist: objects ready for reading
# wlist: objects ready for writing
# xlist: objects with "exceptional conditions"
#
# select.select() raises an exception if the call was interrupted by an
# unwrapped signal (see the PEP 475 for the rationale). You can use
# select.select() as an alternative to signal handlers and non-blocking I/O.

# Returns when a socket is ready for reading.
def get_ready_to_read():
    sockets = [ ]
    sockets.append(sys.stdin)
    sockets.append(socket.socket())

    ready_to
