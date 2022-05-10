import socket
# Test socket.if_indextoname
socket.if_indextoname(0)
try:
    socket.if_indextoname(-1)
except ValueError:
    pass
else:
    print('ValueError expected')
try:
    socket.if_indextoname(0xFFFFFFFF)
except ValueError:
    pass
else:
    print('ValueError expected')


# Test socket.if_nameindex
socket.if_nameindex()


# Test socket.if_nametoindex
socket.if_nametoindex(socket.if_indextoname(0))
try:
    socket.if_nametoindex('')
except ValueError:
    pass
else:
    print('ValueError expected')
try:
    socket.if_nametoindex('X' * 1024)
except ValueError:
    pass
else:
    print('ValueError expected')
