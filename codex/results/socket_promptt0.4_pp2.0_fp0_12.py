import socket
# Test socket.if_indextoname()

import socket
import sys

if len(sys.argv) != 2:
    print(sys.argv[0], "ifindex")
    sys.exit(1)

ifindex = int(sys.argv[1])
name = socket.if_indextoname(ifindex)
print(name)
