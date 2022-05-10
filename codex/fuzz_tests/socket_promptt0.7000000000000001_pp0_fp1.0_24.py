import socket
# Test socket.if_indextoname()
print 'if_indextoname:', socket.if_indextoname(2)

# Test socket.if_nametoindex()
print 'if_nametoindex:', socket.if_nametoindex('lo')

# Test socket.getifaddrs()
print 'getifaddrs:', socket.getifaddrs()

# Test socket.if_nameindex()
print 'if_nameindex:', socket.if_nameindex()
