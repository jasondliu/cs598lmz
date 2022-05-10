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
ifname = socket.if_indextoname(1, 'lo', 'eth0')
print(ifname)
ifname = socket.if_indextoname(1, 'lo', 'eth0', 'wlan0')
print(ifname)

try:
    ifname = socket.if_indextoname(1, 'lo', 'eth0', 'wlan0', 'wlan1')
except ValueError:
    print('ValueError')

try:
    ifname = socket.if_indextoname(1, 'lo', 'eth0', 'wlan0', 'wlan1', 'wlan2')
except ValueError:
    print('ValueError')
