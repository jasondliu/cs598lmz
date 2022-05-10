import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))
print(socket.if_indextoname(2))
print(socket.if_indextoname(3))
print(socket.if_indextoname(4))

# Test socket.if_indextoname() with unknown index
try:
    socket.if_indextoname(5)
except socket.error as e:
    print('if_indextoname(5):', e)

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nameindex() with empty list
print(socket.if_nameindex([]))

# Test socket.if_nameindex() with garbage
try:
    socket.if_nameindex(1)
except TypeError as e:
    print('if_nameindex(1):', e)
try:
    socket.if_nameindex({'a':1})
except TypeError as e:
    print('if_nameindex({\'a\':1}):', e)

# Test
