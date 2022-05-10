import socket
# Test socket.if_indextoname
print(socket.if_indextoname(0))
# Test socket.if_nametoindex
print(socket.if_nametoindex("lo"))
# Test socket.getifaddrs
print(socket.getifaddrs())
