import socket
# Test socket.if_indextoname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(socket.if_indextoname(s.fileno()))
# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))
