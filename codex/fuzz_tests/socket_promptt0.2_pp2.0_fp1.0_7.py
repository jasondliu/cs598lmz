import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if sys.platform == 'darwin':
    print('darwin: skipping')
    sys.exit(0)

ifname = 'lo'
ifindex = socket.if_nametoindex(ifname)
ifname2 = socket.if_indextoname(ifindex)
if ifname != ifname2:
    print('if_nametoindex() and if_indextoname() disagree')
    print('%r != %r' % (ifname, ifname2))
    sys.exit(1)

print('if_nametoindex() and if_indextoname() agree')
print('%r == %r' % (ifname, ifname2))

# Test socket.if_nameindex()

ifnames = [name for _, name in socket.if_nameindex()]
if ifname not in ifnames:
    print('if_nameindex() does not contain %r' % ifname)
    sys.exit(1)

print('if_nameindex() contains %r' % if
