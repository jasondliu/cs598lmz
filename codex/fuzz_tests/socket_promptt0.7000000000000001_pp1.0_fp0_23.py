import socket
# Test socket.if_indextoname()

ifname = socket.if_indextoname(1)
print(socket.if_indextoname(1))
print(socket.if_indextoname(1), ifname)
print(socket.if_indextoname(2), 'lo')
print(socket.if_indextoname(3), 'eth0')

print()
# Test socket.if_nameindex()

print(socket.if_nameindex())
print(socket.if_nameindex())
print(socket.if_nameindex())
print(socket.if_nameindex())
print(socket.if_nameindex())
print(socket.if_nameindex())
print(socket.if_nameindex())

print()
# Test socket.if_nameindex()

print(socket.if_nameindex())
print(socket.if_nameindex())
print(socket.if_nameindex())
print(socket.if_nameindex())

print()
