import socket
socket.if_indextoname(index)

# socket.if_nameindex()
# Return a list of interface tuples
socket.if_nameindex()

# socket.socketpair(family=AF_INET, type=SOCK_STREAM, proto=0)
# Create a pair of connected socket objects using the given address family, socket type, and protocol number
socket.socketpair(socket.AF_INET, socket.SOCK_STREAM, 0)
