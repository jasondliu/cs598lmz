import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform == 'darwin':
    print('darwin: skipping')
    sys.exit(0)

ifname = 'lo'

ifindex = socket.if_nametoindex(ifname)
ifname2 = socket.if_indextoname(ifindex)

if ifname != ifname2:
    print('if_indextoname() failed')
    sys.exit(1)

print('if_indextoname() passed')
sys.exit(0)
