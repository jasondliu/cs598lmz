import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
# Test socket.if_indextoname raises an exception
try:
    socket.if_indextoname(2)
except OSError as e:
    print('[OK]', e)

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.if_nameindex raises an exception
try:
    print(socket.if_nameindex(2))
except OSError as e:
    print('[OK]', e)

# Test socket.if_nametoindex
print(socket.if_nametoindex('lo'))

# Test socket.if_nametoindex raises an exception
try:
    socket.if_nametoindex('eth10')
except OSError as e:
    print('[OK]', e)
