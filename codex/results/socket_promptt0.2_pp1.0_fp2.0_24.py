import socket
# Test socket.if_indextoname()

import socket
import sys

if len(sys.argv) != 2:
    print("usage: if_indextoname.py index")
    sys.exit(2)

index = int(sys.argv[1])

print("if_indextoname({}) -> {}".format(index, socket.if_indextoname(index)))
