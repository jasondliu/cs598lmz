import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
print(socket.if_indextoname(3))
try:
    print(socket.if_indextoname(100))
except OSError as e:
    print(e)
print(socket.if_indextoname(0))
