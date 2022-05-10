import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
print(socket.if_indextoname(1024))
print(socket.if_indextoname(12345))
try:
	print(socket.if_indextoname(1.5))
except TypeError as e:
	print(e)
# Test socket.if_nameindex
print(len(socket.if_nameindex()))
# Test socket.if_nametoindex
print(socket.if_nametoindex('lo'))
print(socket.if_nametoindex('lo0'))
print(socket.if_nametoindex('en0'))
print(socket.if_nametoindex('en1'))
print(socket.if_nametoindex('en2'))
print(socket.if_nametoindex('en3'))
print(socket.if_nametoindex('ppp0'))
print(socket.if_nametoindex('ppp1'))
print(socket.if_nametoindex('fw0'))
print(socket.if_nametoindex('
