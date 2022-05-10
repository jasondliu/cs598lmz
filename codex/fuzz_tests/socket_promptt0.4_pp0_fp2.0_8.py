import socket
# Test socket.if_indextoname()

import socket
import os
import sys

if not hasattr(socket, 'if_indextoname'):
    print('SKIP')
    sys.exit()

ifname = socket.if_indextoname(1)
print(ifname)

# Test socket.if_nameindex()
if not hasattr(socket, 'if_nameindex'):
    print('SKIP')
    sys.exit()

ifs = socket.if_nameindex()
print(ifs)

# Test socket.if_nametoindex()
if not hasattr(socket, 'if_nametoindex'):
    print('SKIP')
    sys.exit()

ifindex = socket.if_nametoindex(ifname)
print(ifindex)
