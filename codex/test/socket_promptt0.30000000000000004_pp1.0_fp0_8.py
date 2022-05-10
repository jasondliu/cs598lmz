import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(1)
except socket.error:
    pass
else:
    print('socket.if_indextoname() works')
