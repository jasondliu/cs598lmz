import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if os.name != 'nt':
    print('This test is only for Windows')
    sys.exit(0)

ifname = socket.if_indextoname(1)
print('Interface name:', ifname)

ifindex = socket.if_nametoindex(ifname)
print('Interface index:', ifindex)

ifindex = socket.if_nametoindex('lo')
print('Interface index:', ifindex)

try:
    ifindex = socket.if_nametoindex('lo0')
except OSError as e:
    print('Error:', e)

try:
    ifname = socket.if_indextoname(0)
except OSError as e:
    print('Error:', e)
