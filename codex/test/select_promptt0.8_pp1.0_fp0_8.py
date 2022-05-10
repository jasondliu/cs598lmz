import select
# Test select.select, which operates on sockets...
# This example is pretty good; the sockets are connected, and there
# is some I/O waiting to be done on the readable socket, and some
# I/O waiting to be done on the writable socket, and some I/O waiting
# to be done on the bad socket.

infds, outfds, errfds = select.select(
    [socket.socket(socket.AF_INET, socket.SOCK_STREAM),
     socket.socket(socket.AF_INET, socket.SOCK_STREAM),
     socket.socket(socket.AF_INET, socket.SOCK_STREAM)],
    [socket.socket(socket.AF_INET, socket.SOCK_STREAM),
     socket.socket(socket.AF_INET, socket.SOCK_STREAM),
     socket.socket(socket.AF_INET, socket.SOCK_STREAM)],
    [])

# set up first socket to be a bad socket
bad_socket = outfds.pop()
bad_socket.close()
