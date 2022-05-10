import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if not hasattr(socket, "if_indextoname"):
    raise SystemExit("socket.if_indextoname not defined -- skipping test_if_indextoname")

ifname = socket.if_indextoname(1)
if ifname != 'lo0':
    raise SystemExit("socket.if_indextoname(1) returned %r, expected 'lo0'" % ifname)

ifindex = socket.if_nametoindex(ifname)
if ifindex != 1:
    raise SystemExit("socket.if_nametoindex('lo0') returned %r, expected 1" % ifindex)

# Test socket.if_nameindex()

if not hasattr(socket, "if_nameindex"):
    raise SystemExit("socket.if_nameindex not defined -- skipping test_if_nameindex")

nameindex = socket.if_nameindex()
if len(nameindex) < 1:
    raise SystemExit("socket.if_nameindex() returned %r, expected at least one
