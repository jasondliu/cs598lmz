import socket
# Test socket.if_indextoname

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
index = s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE)
