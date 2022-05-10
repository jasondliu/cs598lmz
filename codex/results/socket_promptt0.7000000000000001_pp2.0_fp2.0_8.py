import socket
# Test socket.if_indextoname()

if not hasattr(socket, 'if_indextoname'):
    print('SKIP')
    raise SystemExit

# test valid index
print(socket.if_indextoname(2))

# test invalid index
try:
    socket.if_indextoname(1000000)
except OSError:
    print('OSError')

# test invalid type
try:
    socket.if_indextoname('some string')
except TypeError:
    print('TypeError')
