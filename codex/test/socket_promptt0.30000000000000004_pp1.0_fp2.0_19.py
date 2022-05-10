import socket
# Test socket.if_indextoname()

try:
    socket.if_indextoname(0)
except OSError as e:
    print(e.errno)
    print(e)

print('if_indextoname:', socket.if_indextoname(0))

try:
    socket.if_indextoname(1)
except OSError as e:
    print(e.errno)
    print(e)

print('if_indextoname:', socket.if_indextoname(1))

try:
    socket.if_indextoname(2)
except OSError as e:
    print(e.errno)
    print(e)

print('if_indextoname:', socket.if_indextoname(2))

try:
    socket.if_indextoname(3)
except OSError as e:
    print(e.errno)
    print(e)

