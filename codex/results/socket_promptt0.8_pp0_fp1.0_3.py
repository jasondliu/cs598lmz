import socket
# Test socket.if_indextoname() and socket.if_nameindex()
try:
    socket.if_nametoindex("lo")
except:
    print("socket.if_nametoindex() not supported")
else:
    print("socket.if_nametoindex() is supported")
try:
    socket.if_indextoname(1)
except:
    print("socket.if_indextoname() not supported")
else:
    print("socket.if_indextoname() is supported")
