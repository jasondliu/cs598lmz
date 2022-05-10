import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
print(socket.if_indextoname(2))
print(socket.if_indextoname(3))
print(socket.if_indextoname(4))
# Test socket.if_indextoname with an invalid index
try:
    print(socket.if_indextoname(5))
except Exception as err:
    print(err)
