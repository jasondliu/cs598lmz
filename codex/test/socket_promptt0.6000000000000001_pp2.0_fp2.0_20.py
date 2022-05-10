import socket
# Test socket.if_indextoname()

import socket
import sys

print(socket.if_indextoname(1))
print(socket.if_indextoname(1, 'eth0'))
print(socket.if_indextoname(1, 'eth1'))
print(socket.if_indextoname(1, 'lo'))
print(socket.if_indextoname(2))
print(socket.if_indextoname(2, 'eth1'))
print(socket.if_indextoname(2, 'lo'))

try:
    print(socket.if_indextoname(3))
except OSError:
    print('Failed to find index 3')

try:
    print(socket.if_indextoname(1, 'eth2'))
except OSError:
    print('Failed to find index 1 with name "eth2"')
