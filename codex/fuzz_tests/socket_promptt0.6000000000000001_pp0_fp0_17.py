import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform != 'linux':
    print('Test only supported on Linux')
    sys.exit(0)

try:
    socket.if_indextoname(1)
except OSError as e:
    if e.errno != errno.ENXIO:
        print('Unexpected error:', e)
        sys.exit(1)
else:
    print('if_indextoname(1) expected to fail')
    sys.exit(1)

name = socket.if_indextoname(2)
if name != 'eth0':
    print('if_indextoname(2) returned', repr(name))
    sys.exit(1)

print('Tests passed')
