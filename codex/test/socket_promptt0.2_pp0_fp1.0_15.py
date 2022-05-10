import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if os.name != 'nt':
    print('This test is only for Windows')
    sys.exit(0)

if sys.platform == 'win32':
    import _winapi
    if not hasattr(_winapi, 'if_indextoname'):
        print('This test is only for Windows Vista and later')
        sys.exit(0)

if_indextoname = socket.if_indextoname

