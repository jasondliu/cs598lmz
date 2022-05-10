import socket
# Test socket.if_indextoname() function

try:
    socket.if_indextoname(0)
except OSError:
    print('SKIP')
    raise SystemExit

print(socket.if_indextoname(socket.if_nametoindex('lo')))

try:
    socket.if_indextoname(-1)
except OSError:
    print('no negative indexes')

try:
    socket.if_inde
