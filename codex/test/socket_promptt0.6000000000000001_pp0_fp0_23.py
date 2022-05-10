import socket
# Test socket.if_indextoname()

from test_support import get_attribute

socket.if_indextoname(1)

if get_attribute(socket, "if_nameindex") is not None:
    idx = socket.if_nameindex()
    if idx:
        socket.if_indextoname(idx[0][0])
