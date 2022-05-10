import socket
# Test socket.if_indextoname() on a non-existing interface index.
# This should raise ValueError, but currently raises OSError.
import sys
try:
    socket.if_indextoname(-1)
except ValueError:
    print('ValueError')
except OSError:
    print(sys.exc_info()[1])
else:
    print('OSError')
