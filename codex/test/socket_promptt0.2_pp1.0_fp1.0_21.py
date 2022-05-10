import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if not hasattr(socket, "if_indextoname"):
    raise SystemExit("socket.if_indextoname not defined -- skipping test_if_indextoname")

ifname = socket.if_indextoname(1)
if ifname != 'lo0':
    raise SystemExit("socket.if_indextoname(1) returned %r, expected 'lo0'" % (ifname,))

ifname = socket.if_indextoname(2)
if ifname != 'en0':
    raise SystemExit("socket.if_indextoname(2) returned %r, expected 'en0'" % (ifname,))

ifname = socket.if_indextoname(3)
if ifname != 'en1':
    raise SystemExit("socket.if_indextoname(3) returned %r, expected 'en1'" % (ifname,))

ifname = socket.if_indextoname(4)
