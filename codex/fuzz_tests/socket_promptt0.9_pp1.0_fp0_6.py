import socket
# Test socket.if_indextoname() w/o cap
for i in range(100):
    socket.if_indextoname(i)
