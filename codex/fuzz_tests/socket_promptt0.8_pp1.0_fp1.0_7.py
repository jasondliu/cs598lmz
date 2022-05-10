import socket
# Test socket.if_indextoname() in the IPv4 and IPv6 cases.
print(socket.if_indextoname(1))
print(socket.if_indextoname(20))
print(socket.if_indextoname(32))
print(socket.if_indextoname(256))
print(socket.if_indextoname(1024))
