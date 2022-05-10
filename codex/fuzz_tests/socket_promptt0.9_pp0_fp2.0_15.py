import socket
# Test socket.if_indextoname
print(socket.if_indextoname(0))
print(socket.if_indextoname(3))
print(socket.if_indextoname(4))
print(socket.if_indextoname(5))
# Test socket.if_nametoindex
print(socket.if_nametoindex('lo'))
#print(socket.if_nametoindex('tun'))
print(socket.if_nametoindex('eth0'))
print(socket.if_nametoindex('eth1'))
print(socket.if_nametoindex('eth2'))
