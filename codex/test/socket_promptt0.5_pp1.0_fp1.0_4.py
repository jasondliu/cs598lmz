import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if sys.platform == 'darwin':
    print('skipped on darwin')
    sys.exit(0)

if sys.platform == 'win32':
    print('skipped on windows')
    sys.exit(0)

if not hasattr(socket, 'if_indextoname'):
    print('skipped: if_indextoname not supported')
    sys.exit(0)

if_indextoname = socket.if_indextoname

# get the interface index of 'lo'
index = socket.if_nametoindex('lo')

# get the interface name of the index
name = if_indextoname(index)

# check if it is 'lo'
if name != 'lo':
    print('failed to get the name of the loopback device: %s' % name)
    sys.exit(1)

# get the interface index of 'lo', this time using a buffer
buf = bytearray(256)
index = socket.if_nameto
