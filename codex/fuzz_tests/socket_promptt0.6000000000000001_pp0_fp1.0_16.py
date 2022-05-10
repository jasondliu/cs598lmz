import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform.startswith('linux'):
    try:
        socket.if_indextoname(1)
    except OSError:
        print('SKIP')
        sys.exit()

print(socket.if_indextoname(1))
print(socket.if_indextoname(2))
print(socket.if_indextoname(3))
print(socket.if_indextoname(4))
print(socket.if_indextoname(5))
print(socket.if_indextoname(6))
