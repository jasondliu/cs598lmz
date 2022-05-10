import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
print(socket.if_indextoname(2))
# Test socket.if_nameindex
print(socket.if_nameindex())
print(socket.if_nameindex()[0])
print(socket.if_nameindex()[0][0])
print(socket.if_nameindex()[0][1])
print(socket.if_nameindex()[1])
print(socket.if_nameindex()[1][0])
print(socket.if_nameindex()[1][1])
print(socket.if_nameindex()[2])
print(socket.if_nameindex()[2][0])
print(socket.if_nameindex()[2][1])
