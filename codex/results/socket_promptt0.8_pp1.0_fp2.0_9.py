import socket
# Test socket.if_indextoname() on non-existing index
try:
    socket.if_indextoname(1)
    raise Exception("if_indextoname(1) didn't raise OSError")
except OSError:
    pass
