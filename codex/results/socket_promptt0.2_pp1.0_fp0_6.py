import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform == 'darwin':
    print('darwin: skipping test')
    sys.exit(0)

ifname = socket.if_indextoname(1)
print(ifname)
ifname = socket.if_indextoname(1, 'lo')
print(ifname)

try:
    socket.if_indextoname(1, 'lo', 'lo')
except TypeError:
    print('TypeError')

try:
    socket.if_indextoname(1, 'lo', 'lo', 'lo')
except TypeError:
    print('TypeError')

try:
    socket.if_indextoname(1, 'lo', 'lo', 'lo', 'lo')
except TypeError:
    print('TypeError')

try:
    socket.if_indextoname(1, 'lo', 'lo', 'lo', 'lo', 'lo')
except TypeError:
    print('TypeError')

try:
    socket.if_indextoname
