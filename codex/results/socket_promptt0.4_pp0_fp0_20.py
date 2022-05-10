import socket
# Test socket.if_indextoname()

if not hasattr(socket, 'if_indextoname'):
    print('SKIP')
    raise SystemExit

print(socket.if_indextoname(1))
print(socket.if_indextoname(1, True))

try:
    socket.if_indextoname(0)
except OSError:
    print('OSError')

try:
    socket.if_indextoname(1, False)
except OSError:
    print('OSError')
