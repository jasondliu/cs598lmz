import socket
# Test socket.if_indextoname(3)

from test_support import verbose, TestFailed

if_names = socket.if_indextoname(3)

