import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
print(socket.if_indextoname(0))
print(socket.if_indextoname(-1))

print(socket.if_indextoname(1, True))
print(socket.if_indextoname(0, True))
print(socket.if_indextoname(-1, True))

# Test socket.if_nametoindex
print(socket.if_nametoindex('lo'))
print(socket.if_nametoindex('eth0'))
print(socket.if_nametoindex('eth1'))
print(socket.if_nametoindex('eth2'))
print(socket.if_nametoindex('eth3'))
print(socket.if_nametoindex('eth4'))
print(socket.if_nametoindex('eth5'))
print(socket.if_nametoindex('eth6'))
print(socket.if_nametoindex('eth7'))

print(socket.if_nametoindex('lo', True))
