import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if not hasattr(socket, "if_indextoname"):
    print("SKIP")
    sys.exit()

ifname = socket.if_indextoname(1)
if ifname:
    print(ifname)
else:
    print("None")

# Test socket.if_nameindex()
ifname = socket.if_nameindex()
print(ifname)

# Test socket.if_nameindex()
ifname = socket.if_nameindex(1)
print(ifname)

# Test socket.if_nameindex()
ifname = socket.if_nameindex(1, 2)
print(ifname)

# Test socket.if_nameindex()
ifname = socket.if_nameindex(1, 2, 3)
print(ifname)

# Test socket.if_nameindex()
ifname = socket.if_nameindex(1, 2, 3, 4)
print(ifname)

# Test socket.if_nameindex()
ifname = socket
