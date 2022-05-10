import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if not hasattr(socket, 'if_indextoname'):
    raise ImportError('need socket.if_indextoname()')

ifname = socket.if_indextoname(1)
if ifname != 'lo':
    print('socket.if_indextoname(1) = %r, expected "lo"' % (ifname,))
    sys.exit(1)

ifindex = socket.if_nametoindex(ifname)
if ifindex != 1:
    print('socket.if_nametoindex("lo") = %r, expected 1' % (ifindex,))
    sys.exit(1)

# Find a non-lo interface
for ifname in os.listdir('/sys/class/net'):
    if ifname == 'lo':
        continue
    break

ifindex = socket.if_nametoindex(ifname)
ifindex2 = socket.if_nametoindex(ifname)
