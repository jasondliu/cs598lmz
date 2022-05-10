import socket
# Test socket.if_indextoname() on all interfaces
for i in range(0, socket.if_nametoindex('')):
    print(socket.if_indextoname(i))

# Test socket.if_nametoindex() on some interfaces
print(socket.if_nametoindex('lo'))
print(socket.if_nametoindex('eth0'))
print(socket.if_nametoindex('eth0.0'))

# Test socket.if_nameindex()
for name, index in socket.if_nameindex():
    print(name, index)
