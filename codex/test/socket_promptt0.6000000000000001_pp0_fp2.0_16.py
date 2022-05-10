import socket
# Test socket.if_indextoname using a numeric index.
import socket
import sys
import test_support

if hasattr(socket, 'if_indextoname'):
    try:
        socket.if_indextoname(0)
    except socket.error:
        pass
