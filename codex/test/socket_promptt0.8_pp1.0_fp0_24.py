import socket
# Test socket.if_indextoname
for i in range(1,255):
	print(socket.if_indextoname(i))
print('\n')
# Test socket.if_nametoindex
for i in range(1,255):
	print(socket.if_nametoindex(socket.if_indextoname(i)))
print('\n')
