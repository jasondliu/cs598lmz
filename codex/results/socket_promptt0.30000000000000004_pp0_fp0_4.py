import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if sys.platform == 'darwin':
    print('darwin: skipping test')
    sys.exit(0)

if not hasattr(socket, 'if_indextoname'):
    print('socket.if_indextoname() not found')
    sys.exit(0)

ifname = socket.if_indextoname(1)
print(ifname)

try:
    socket.if_indextoname(0)
except OSError as err:
    print(err)

try:
    socket.if_indextoname(-1)
except OSError as err:
    print(err)

try:
    socket.if_indextoname(os.sysconf('SC_NET_IF_MAX'))
except OSError as err:
    print(err)

try:
    socket.if_indextoname(os.sysconf('SC_NET_IF_MAX') + 1)
except OSError as err:
    print
