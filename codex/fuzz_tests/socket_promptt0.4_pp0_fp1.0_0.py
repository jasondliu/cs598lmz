import socket
# Test socket.if_indextoname()
#
# This test is expected to fail on Windows, because the function is not
# implemented.

import socket
import sys

if sys.platform == 'win32':
    print('SKIP')
    sys.exit()

if_name = socket.if_indextoname(1)
if_index = socket.if_nametoindex(if_name)
print(if_name)
print(if_index)
