import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform == 'win32':
    print('Windows')
    sys.exit(0)

print(socket.if_indextoname(1))
