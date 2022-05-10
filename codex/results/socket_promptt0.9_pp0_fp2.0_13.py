import socket
# Test socket.if_indextoname()
# (Bug #804467, #827742)

try:
    socket.if_indextoname(1)
except socket.error:
    pass
else:
    raise Exception("No exception raised")
