import socket
# Test socket.if_indextoname()

try:
    socket.if_indextoname(0)
except socket.error as e:
    print('if_indextoname:', e.args[0])
else:
    print('if_indextoname:', socket.if_indextoname(0))

try:
    socket.if_indextoname(0xffffffff)
except socket.error as e:
    print('if_indextoname:', e.args[0])
else:
    print('if_indextoname:', socket.if_indextoname(0xffffffff))

# Test socket.if_indextoname()

try:
    socket.if_nametoindex('')
except socket.error as e:
    print('if_nametoindex:', e.args[0])
else:
    print('if_nametoindex:', socket.if_nametoindex(''))

