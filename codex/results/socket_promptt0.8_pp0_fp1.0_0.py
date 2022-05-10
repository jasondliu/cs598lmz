import socket
# Test socket.if_indextoname() method

print '\nSocket names:', socket.if_nameindex()
print '\nLoopback name:', socket.if_indextoname(1)
