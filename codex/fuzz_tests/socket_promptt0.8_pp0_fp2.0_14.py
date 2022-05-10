import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(3))
# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))
# Test socket.getinterface()
print(socket.getinterface('127.0.0.1'))
