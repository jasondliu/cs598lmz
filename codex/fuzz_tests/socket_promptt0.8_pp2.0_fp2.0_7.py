import socket
# Test socket.if_indextoname()

print(socket.if_indextoname(1))
print(socket.if_indextoname(2))
print(socket.if_indextoname(3))
print(socket.if_indextoname(65535))

print(socket.if_indextoname(1, 'eth0'))
print(socket.if_indextoname(2, 'eth1'))
print(socket.if_indextoname(3, 'br-2151a8dae7d5'))
print(socket.if_indextoname(65535, 'lo'))

# Zero is not a valid index.
try:
    socket.if_indextoname(0)
except ValueError:
    print('ValueError')

# Negative value is not a valid index.
try:
    socket.if_indextoname(-1)
except ValueError:
    print('ValueError')

# Index greater than 65535 is not valid.
try:
    socket.if_indextoname(65536)
except ValueError
