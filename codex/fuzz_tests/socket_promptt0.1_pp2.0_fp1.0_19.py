import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if os.name != 'nt':
    print('This test is only for Windows')
    sys.exit(0)

ifname = socket.if_indextoname(1)
print('if_indextoname(1) -> %s' % ifname)

ifname = socket.if_indextoname(2)
print('if_indextoname(2) -> %s' % ifname)

ifname = socket.if_indextoname(3)
print('if_indextoname(3) -> %s' % ifname)

ifname = socket.if_indextoname(4)
print('if_indextoname(4) -> %s' % ifname)

ifname = socket.if_indextoname(5)
print('if_indextoname(5) -> %s' % ifname)

ifname = socket.if_indextoname(6)
print('if_indextoname(6) -> %s' % ifname
