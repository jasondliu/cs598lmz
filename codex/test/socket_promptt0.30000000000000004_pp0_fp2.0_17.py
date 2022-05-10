import socket
# Test socket.if_indextoname()

import socket
import sys
import os

if sys.platform == 'win32':
    print('Windows does not support this test')
    sys.exit(0)

if_index = socket.if_nametoindex('lo')
if_name = socket.if_indextoname(if_index)

if if_name != 'lo':
    print('if_indextoname() failed')
    sys.exit(1)

print('if_indextoname() passed')
