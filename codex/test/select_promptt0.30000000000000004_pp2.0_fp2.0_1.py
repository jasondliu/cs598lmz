import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# Example:

# import select
# import socket
# import time

# s = socket.socket()

# # become a server socket
# s.bind(('localhost', 5000))
# s.listen(5)

# while True:
#     # determine which sockets are ready to be read from
#     # and which are ready to be written to
#     rlist, wlist, xlist = select.select([s], [], [], 5)

#     # if the server socket is ready to be read from,
#     # that means there is a new connection
#     if s in rlist:
#         client_socket, address = s.accept()
#         print('Got connection from', address)
#         #
