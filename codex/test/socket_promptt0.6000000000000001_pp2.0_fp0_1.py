import socket
# Test socket.if_indextoname()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# These are the names of the interfaces on my Mac
# Inet6 is the IPv6 address
print(socket.if_indextoname(sock.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, 1)))
print(socket.if_indextoname(sock.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, 2)))
print(socket.if_indextoname(sock.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, 3)))
print(socket.if_indextoname(sock.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, 4)))
print(socket.if_indextoname(sock.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, 5)))

# This is the index
