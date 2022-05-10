import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if os.name != 'nt':
    print('This test only runs on Windows')
    sys.exit(0)

if_indextoname = socket.if_indextoname

# Test invalid index
try:
    if_indextoname(-1)
except OSError as e:
    if e.winerror != 10049:
        raise
else:
    raise RuntimeError('expected OSError')

# Test valid index
name = if_indextoname(1)
if name != 'Loopback Pseudo-Interface 1':
    raise RuntimeError('expected "Loopback Pseudo-Interface 1", got %r' % name)
