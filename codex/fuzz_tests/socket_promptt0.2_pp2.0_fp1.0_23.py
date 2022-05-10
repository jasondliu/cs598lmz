import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform == 'win32':
    print('Windows does not support this test')
    sys.exit(0)

ifname = socket.if_indextoname(1)
print('if_indextoname(1) -> %s' % ifname)

ifname = socket.if_indextoname(1)
print('if_indextoname(1) -> %s' % ifname)

ifname = socket.if_indextoname(1)
print('if_indextoname(1) -> %s' % ifname)

ifname = socket.if_indextoname(1)
print('if_indextoname(1) -> %s' % ifname)

ifname = socket.if_indextoname(1)
print('if_indextoname(1) -> %s' % ifname)

ifname = socket.if_indextoname(1)
print('if_indextoname(1) -> %s' % ifname)

