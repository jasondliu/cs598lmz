import socket
# Test socket.if_indextoname() by passing an invalid interface index.
try:
    socket.if_indextoname(-1)
except Exception as e:
    print(e)
