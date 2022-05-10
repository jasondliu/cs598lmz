import select
# Test select.select()
#
# select() -- monitors multiple file descriptors, returning
#             whenever a monitored file descriptor becomes
#             ready for some class of I/O operation
#
# select() takes 3 lists of file descriptors:
#           rlist -- wait until ready for reading
#           wlist -- wait until ready for writing
#           xlist -- wait for an "exceptional condition"
#
# select() can also take a 4th, optional argument:
#           timeout -- a time-out as a float value,
#                      in seconds
#
# select() returns 3 lists of file descriptors:
#           rlist -- those sockets ready for reading
#           wlist -- those sockets ready for writing
#           xlist -- those sockets with an "exceptional condition"


# Create a pair of connected sockets

# Note the result of socketpair() is a pair of
# connected sockets that can be used to pass data
# back and forth.  This is good for interprocess
# communication.

socks = []

for res in socket.getaddrinfo(None, 0, socket.AF_UNSPEC,
                              socket
