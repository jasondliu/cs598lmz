import socket
# Test socket.if_indextoname support
print "Interface index: %d" % socket.if_nametoindex("lo")
print "Interface name: %s" % socket.if_indextoname(1)
