import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if not hasattr(socket, "if_indextoname"):
    print("SKIP")
    sys.exit()

# Test invalid args
try:
    socket.if_indextoname(0, "")
except OSError:
    print("OSError")

# Test invalid index
try:
    socket.if_indextoname(1)
except OSError:
    print("OSError")

# Test valid index
print(socket.if_indextoname(0))

# Test valid index with family
print(socket.if_indextoname(0, socket.AF_INET))
