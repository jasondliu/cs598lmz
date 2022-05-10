import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform == 'darwin':
    print('darwin: skipping test')
    sys.exit(0)

if sys.platform == 'win32':
    print('win32: skipping test')
    sys.exit(0)

ifname = socket.if_indextoname(1)
print(ifname)
