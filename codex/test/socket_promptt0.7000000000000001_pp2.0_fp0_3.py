import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(3))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.if_addrtoname()
print(socket.if_addrtoname(3, '\x7f\x00\x00\x01'))
print(socket.if_addrtoname(3, '\x7f\x00\x00\x02'))
print(socket.if_addrtoname(3, '\x7f\x00\x00\x03'))
print(socket.if_addrtoname(3, '\x7f\x00\x00\x04'))
print(socket.if_addrtoname(3, '\x7f\x00\x00\x05'))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_addrindex()
