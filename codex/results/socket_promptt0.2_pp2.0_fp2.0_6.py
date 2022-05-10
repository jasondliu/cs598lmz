import socket
# Test socket.if_indextoname()

import socket
import sys

if not hasattr(socket, 'if_indextoname'):
    print('SKIP')
    sys.exit()

print(socket.if_indextoname(1))
