import socket
# Test socket.if_indextoname()

import socket
import sys

if not hasattr(socket, 'if_indextoname'):
    print('SKIP')
    sys.exit()

# Get interface name from index
print(socket.if_indextoname(1))

# Get interface index from name
print(socket.if_nametoindex('lo'))

# Get interface index from non-existent name
try:
    socket.if_nametoindex('no-such-interface')
except OSError as e:
    print(e.args[0])

# Get interface name from non-existent index
try:
    socket.if_indextoname(99999)
except OSError as e:
    print(e.args[0])
