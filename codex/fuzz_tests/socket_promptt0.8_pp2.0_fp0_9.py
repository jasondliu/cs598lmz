import socket
# Test socket.if_indextoname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE), 0))
