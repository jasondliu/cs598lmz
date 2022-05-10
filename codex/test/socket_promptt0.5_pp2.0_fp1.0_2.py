import socket
# Test socket.if_indextoname()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Testing socket.if_indextoname()")

print("    socket.if_indextoname(0): %s" % socket.if_indextoname(0))
print("    socket.if_indextoname(-1): %s" % socket.if_indextoname(-1))
