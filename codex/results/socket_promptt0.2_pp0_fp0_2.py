import socket
# Test socket.if_indextoname()

import sys
import socket

if len(sys.argv) != 2:
    print("usage: if_indextoname.py index")
    sys.exit(2)

index = int(sys.argv[1])

try:
    name = socket.if_indextoname(index)
except ValueError:
    print("invalid index")
    sys.exit(1)

print(name)
