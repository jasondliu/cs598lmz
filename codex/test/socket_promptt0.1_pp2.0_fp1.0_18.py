import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform == 'win32':
    print('Windows')
    sys.exit(0)

if sys.platform.startswith('linux'):
    print('Linux')
    sys.exit(0)

if sys.platform == 'darwin':
    print('Mac OS X')
    sys.exit(0)

print('Unsupported platform')
sys.exit(1)
