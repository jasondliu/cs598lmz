import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform == 'darwin':
    print('skipping test on MacOS')
    sys.exit(0)

ifname = socket.if_indextoname(1)
print(ifname)
