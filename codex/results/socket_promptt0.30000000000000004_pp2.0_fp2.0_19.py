import socket
# Test socket.if_indextoname()

from test import support

if not hasattr(socket, 'if_indextoname'):
    raise support.TestSkipped("if_indextoname not available")

name = socket.if_indextoname(1)
if name is None:
    raise support.TestSkipped("if_indextoname not available")

if name == 'lo':
    raise support.TestSkipped("if_indextoname not available")
