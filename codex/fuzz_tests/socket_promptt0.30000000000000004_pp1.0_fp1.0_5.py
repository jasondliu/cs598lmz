import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform == 'darwin':
    print('darwin')
    sys.exit(0)

if sys.platform.startswith('freebsd'):
    print('freebsd')
    sys.exit(0)

if sys.platform.startswith('netbsd'):
    print('netbsd')
    sys.exit(0)

if sys.platform.startswith('openbsd'):
    print('openbsd')
    sys.exit(0)

if sys.platform.startswith('linux'):
    print('linux')
    sys.exit(0)

print('unsupported platform')
sys.exit(1)
