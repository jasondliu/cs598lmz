import socket
# Test socket.if_indextoname
socket.if_indextoname(1)
socket.if_indextoname(1, 'a')
try:
    socket.if_indextoname(1, 'a', 'b')
except TypeError:
    pass
try:
    socket.if_indextoname()
except TypeError:
    pass
try:
    socket.if_indextoname(1, 'a', 'b', 'c')
except TypeError:
    pass

# Test socket.if_nameindex
socket.if_nameindex()
socket.if_nameindex(1)
try:
    socket.if_nameindex(1, 2)
except TypeError:
    pass
try:
    socket.if_nameindex(1, 2, 3)
except TypeError:
    pass
try:
    socket.if_nameindex(1, 2, 3, 4)
except TypeError:
    pass

# Test socket.if_nametoindex
socket.if_nametoindex('lo')
socket.if_nametoindex('lo', 'a')

