import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.if_nameindex()
l = socket.if_nameindex()
print(l)
print(l[0][0])
print(l[0][1])

# Test socket.if_freenameindex()
socket.if_freenameindex(l)

# Test socket.if_indextoname()
print(socket.if_indextoname(0))

# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_indextoname()
print(socket.if_indextoname(2))

# Test socket.if_indextoname()
print(socket.if_indextoname(3))

# Test socket.if_indextoname()
print(socket.if_indextoname(4))

# Test socket.if_indext
