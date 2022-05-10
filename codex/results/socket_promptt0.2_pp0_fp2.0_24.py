import socket
# Test socket.if_indextoname()

import socket
import sys

if len(sys.argv) != 2:
    print('usage: if_indextoname.py interface_index')
    sys.exit(2)

index = int(sys.argv[1])

try:
    print(socket.if_indextoname(index))
except ValueError as err:
    print('ERROR: %s' % str(err))
