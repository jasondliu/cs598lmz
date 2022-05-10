import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform != 'win32':
    print('This test is only for Windows')
    sys.exit(0)

if sys.version_info[:2] < (2, 7):
    print('This test is only for Python 2.7 or later')
    sys.exit(0)

ifname = 'Local Area Connection'
ifindex = socket.if_nametoindex(ifname)
if ifindex == 0:
    print('if_nametoindex() failed')
    sys.exit(1)

ifname2 = socket.if_indextoname(ifindex)
if ifname2 != ifname:
    print('if_indextoname() failed')
    sys.exit(1)

print('if_indextoname() works')
