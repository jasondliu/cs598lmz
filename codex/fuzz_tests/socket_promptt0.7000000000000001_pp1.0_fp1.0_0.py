import socket
# Test socket.if_indextoname()

try:
    socket.if_indextoname(socket.if_nametoindex('lo'))
except:
    print('SKIP')
    raise SystemExit

print(socket.if_indextoname(socket.if_nametoindex('lo')))
try:
    socket.if_indextoname(socket.if_nametoindex('lo') + 1)
except:
    print('socket.error')
