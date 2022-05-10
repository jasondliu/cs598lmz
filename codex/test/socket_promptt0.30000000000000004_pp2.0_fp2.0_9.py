import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform == 'darwin':
    print('darwin: skipping test')
    sys.exit(0)

if_index = socket.if_nametoindex('lo')
if_name = socket.if_indextoname(if_index)

print('lo: if_index=%d, if_name=%s' % (if_index, if_name))
