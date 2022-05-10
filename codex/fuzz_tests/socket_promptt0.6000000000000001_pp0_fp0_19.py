import socket
# Test socket.if_indextoname
for i in range(0, 10000):
    try:
        socket.if_indextoname(i)
    except ValueError:
        pass

try:
    socket.if_indextoname(-1)
except ValueError:
    pass

try:
    socket.if_indextoname(0xffffffff)
except ValueError:
    pass

# Test socket.if_nametoindex
for i in range(0, 10000):
    try:
        socket.if_nametoindex(socket.if_indextoname(i))
    except ValueError:
        pass

try:
    socket.if_nametoindex('bad_if_name')
except ValueError:
    pass

# Test socket.if_nameindex
socket.if_nameindex()

# Test socket.if_freenameindex
socket.if_freenameindex(socket.if_nameindex())
