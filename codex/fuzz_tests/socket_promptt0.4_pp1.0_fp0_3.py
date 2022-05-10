import socket
# Test socket.if_indextoname
import socket
import sys

if sys.platform == 'win32':
    print('Windows does not support this test')
    sys.exit(0)

try:
    socket.if_indextoname(1)
except OSError as e:
    print(e)
    if e.errno != errno.ENXIO:
        raise

# Test socket.if_nameindex
import socket
import sys

if sys.platform == 'win32':
    print('Windows does not support this test')
    sys.exit(0)

try:
    socket.if_nameindex()
except OSError as e:
    print(e)
    if e.errno != errno.ENXIO:
        raise

# Test socket.if_nametoindex
import socket
import sys

if sys.platform == 'win32':
    print('Windows does not support this test')
    sys.exit(0)

try:
    socket.if_nametoindex('lo')
except OSError as e:
    print(e
