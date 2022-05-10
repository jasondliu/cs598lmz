import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if not hasattr(socket, "if_indextoname"):
    raise SystemExit("socket.if_indextoname not defined -- skipping test_if_indextoname")

ifname = socket.if_indextoname(1)
if ifname != 'lo':
    raise SystemExit("socket.if_indextoname(1) returned %s, expected 'lo'" % ifname)

ifindex = socket.if_nametoindex(ifname)
if ifindex != 1:
    raise SystemExit("socket.if_nametoindex('lo') returned %d, expected 1" % ifindex)

ifindex = socket.if_nametoindex('lo0')
if ifindex != 0:
    raise SystemExit("socket.if_nametoindex('lo0') returned %d, expected 0" % ifindex)

try:
    ifindex = socket.if_nametoindex('lo1')
except OSError:
    pass
