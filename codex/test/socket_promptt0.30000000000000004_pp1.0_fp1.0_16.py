import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if len(sys.argv) != 2:
    print >>sys.stderr, "usage: %s <interface-index>" % sys.argv[0]
    sys.exit(1)

index = int(sys.argv[1])
try:
    name = socket.if_indextoname(index)
except OSError as e:
    print >>sys.stderr, "if_indextoname(%d): %s" % (index, e)
    sys.exit(1)

