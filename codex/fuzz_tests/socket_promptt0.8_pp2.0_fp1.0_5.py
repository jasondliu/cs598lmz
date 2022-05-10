import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))
print(socket.if_indextoname(10))
print(socket.if_indextoname(1000))
# Test socket.if_nameindex()
for idx, name in socket.if_nameindex():
	print(idx, name)
