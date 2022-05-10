import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if os.name != 'nt':
    print('This test is only for Windows')
    sys.exit(0)

if_indextoname = socket.if_indextoname

# Test invalid index
try:
    if_indextoname(-1)
except OSError as e:
    if e.errno != 10049:
        raise

# Test valid index
if_indextoname(1)
