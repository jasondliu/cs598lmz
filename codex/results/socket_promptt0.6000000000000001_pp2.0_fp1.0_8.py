import socket
# Test socket.if_indextoname
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 0))
print(socket.if_indextoname(s.getsockname()[1]))
