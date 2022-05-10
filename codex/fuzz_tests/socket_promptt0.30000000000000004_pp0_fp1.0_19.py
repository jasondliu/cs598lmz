import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if os.name != 'nt':
    print('if_indextoname() is only supported on Windows')
    sys.exit(0)

if not hasattr(socket, 'if_indextoname'):
    print('if_indextoname() not found')
    sys.exit(0)

ifname = socket.if_indextoname(1)
print('if_indextoname(1) ->', ifname)
print('if_indextoname(1) ->', socket.if_indextoname(1))
print('if_indextoname(1) ->', socket.if_indextoname(1))
print('if_indextoname(1) ->', socket.if_indextoname(1))
print('if_indextoname(1) ->', socket.if_indextoname(1))
print('if_indextoname(1) ->', socket.if_indextoname(1))
print('if_indextoname(1
