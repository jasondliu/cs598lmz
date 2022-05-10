import select
# Test select.select()
#
# This function is used to multiplex among several file descriptors.
#
# select.select(rlist, wlist, xlist[, timeout])
#
#     rlist: wait until ready for reading
#     wlist: wait until ready for writing
#     xlist: wait for an "exceptional condition"
#     timeout: in seconds; may be 0, None or float value
#
# Returns three lists corresponding to the first three arguments
#
# EINTR error: The system call was interrupted by a signal that was
# caught before a valid timeout expiration occurred.
#
# (read_ready, write_ready, exceptional) = select.select(rlist, wlist, xlist[, timeout])
#
# Note: select() modifies the lists it is given, so you should pass in
# copies of the original lists.
#
# Example:
#
#     import select
#     import socket
#
#     s = socket.socket()
#     s.connect(('www.python.org', 80))
#     s.setblocking(0)
#     s.
