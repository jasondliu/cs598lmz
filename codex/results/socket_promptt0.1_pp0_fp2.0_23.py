import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if not hasattr(socket, "if_indextoname"):
    print("SKIP")
    sys.exit()

# Test invalid index
try:
    socket.if_indextoname(0)
except OSError:
    print("OSError")

# Test valid index
ifname = socket.if_indextoname(1)
print(ifname)

# Test valid index with invalid length
try:
    socket.if_indextoname(1, 0)
except OSError:
    print("OSError")

# Test valid index with valid length
ifname = socket.if_indextoname(1, len(ifname))
print(ifname)

# Test valid index with valid length
ifname = socket.if_indextoname(1, len(ifname) + 1)
print(ifname)

# Test valid index with valid length
ifname = socket.if_indextoname(1, len(ifname) + 1)
print(if
