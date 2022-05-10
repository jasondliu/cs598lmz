import socket
# Test socket.if_indextoname()

print(socket.if_indextoname(1))
print(socket.if_indextoname(0))

try:
    print(socket.if_indextoname(2))
except OSError as e:
    print(e)

try:
    print(socket.if_indextoname(-1))
except OSError as e:
    print(e)
