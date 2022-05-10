import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if not hasattr(socket, 'if_indextoname'):
    print('SKIP')
    sys.exit()

ifname = socket.if_indextoname(1)
print(ifname)

# Test invalid index
try:
    socket.if_indextoname(0)
except OSError:
    print('OSError')

# Test invalid index
try:
    socket.if_indextoname(65536)
except OSError:
    print('OSError')
