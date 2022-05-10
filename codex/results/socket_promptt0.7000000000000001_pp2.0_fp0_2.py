import socket
# Test socket.if_indextoname() function.
#

import sys
import socket

if sys.platform not in ('win32', 'cygwin'):
    # skip test if not on Windows
    sys.exit(0)

for index in [0, 256, 255, 10]:
    try:
        ifname = socket.if_indextoname(index)
    except OSError as e:
        if e.errno != 10049:
            raise
        else:
            print('%d: %s' % (index, e))
            continue
    print('%d: %s' % (index, ifname))
