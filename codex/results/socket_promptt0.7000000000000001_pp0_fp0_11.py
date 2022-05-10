import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(socket.if_nametoindex('lo')))
print(socket.if_indextoname(socket.if_nametoindex('eth0')))
print(socket.if_indextoname(socket.if_nametoindex('')))
print(socket.if_indextoname(socket.if_nametoindex('abc')))
print(socket.if_indextoname(socket.if_nametoindex('a\0')))

# Test socket.if_indextoname() for bad argument
try:
    socket.if_indextoname(65536)
except:
    pass

# Test socket.if_indextoname() for bad argument
try:
    socket.if_indextoname(-1)
except:
    pass
