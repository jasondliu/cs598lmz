import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform == 'darwin':
    print('darwin: skipping test')
    sys.exit(0)

if sys.platform.startswith('linux'):
    print('linux: skipping test')
    sys.exit(0)

if sys.platform.startswith('freebsd'):
    print('freebsd: skipping test')
    sys.exit(0)

print(socket.if_indextoname(1))
