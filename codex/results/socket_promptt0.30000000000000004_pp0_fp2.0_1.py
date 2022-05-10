import socket
# Test socket.if_indextoname()

# This test is specific to Linux.

import sys
if sys.platform != 'linux':
    raise SystemExit('Skip on non-Linux platform')

import socket

ifname = socket.if_indextoname(1)
print(ifname)

# This should raise an exception
try:
    socket.if_indextoname(0)
except OSError as e:
    print(e)
