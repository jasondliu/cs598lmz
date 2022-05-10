import socket
# Test socket.if_indextoname()

print("Test socket.if_indextoname():")
print("  interface index: %s" % (socket.if_indextoname(1)))
print("  interface index: %s" % (socket.if_indextoname(2)))
print("  interface index: %s" % (socket.if_indextoname(3)))
