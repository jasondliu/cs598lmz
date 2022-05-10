import socket
# Test socket.if_indextoname

import socket
import sys

from test_support import verbose

if not hasattr(socket, 'if_indextoname'):
    raise ImportError("socket.if_indextoname not defined -- skipping test_if_indextoname")

