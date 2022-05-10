import socket
# Test socket.if_indextoname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('%s' % socket.if_indextoname(1))
