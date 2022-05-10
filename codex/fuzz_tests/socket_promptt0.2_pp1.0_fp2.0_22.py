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
    print('if_nametoindex(%r) -> %d' % (ifname, ifindex))
    print('if_indextoname(%d) -> %r' % (ifindex, ifname2))
    print('if_nametoindex(%r) != if_indextoname(if_nametoindex(%r))' % (ifname, ifname))
    sys.exit(1)

print('if_nametoindex(%r) -> %d' % (ifname, ifindex))
print('if_indextoname(%d) -> %r' % (ifindex, ifname2))
print('if_nametoindex(%r) == if_indext
