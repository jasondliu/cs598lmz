import socket
# Test socket.if_indextoname()

import socket
import sys

if len(sys.argv) != 2:
    print >>sys.stderr, "usage: %s interface_index" % sys.argv[0]
    sys.exit(1)

interface_index = int(sys.argv[1])
