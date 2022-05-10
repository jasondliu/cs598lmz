import socket
# Test socket.if_indextoname()
import socket

if socket.if_indextoname(0) != 'lo':
    raise RuntimeError("if_indextoname()")
print("if_indextoname():", socket.if_indextoname(0))
print("Socket if_indextoname test passed")
