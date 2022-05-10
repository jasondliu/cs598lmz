import socket
# Test socket.if_indextoname()

print(socket.if_indextoname(1))
print(socket.if_indextoname(1, True))
print(socket.if_indextoname(1, False))

try:
    print(socket.if_indextoname(1, 'a'))
except TypeError:
    print('TypeError')

try:
    print(socket.if_indextoname(1, 1))
except TypeError:
    print('TypeError')

try:
    print(socket.if_indextoname(1, 1.0))
except TypeError:
    print('TypeError')

try:
    print(socket.if_indextoname(1, (1,)))
except TypeError:
    print('TypeError')

try:
    print(socket.if_indextoname(1, [1]))
except TypeError:
    print('TypeError')

try:
    print(socket.if_indextoname(1, {1: 1}))
except TypeError:
    print('
