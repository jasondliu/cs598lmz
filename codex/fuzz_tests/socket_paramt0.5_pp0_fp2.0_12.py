import socket
socket.if_indextoname(3)

socket.if_nametoindex('eth0')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 9999))

print(s.getsockname())

s.recvfrom(8192)

s.recvfrom(8192)

s.recvfrom(8192)

s.recvfrom(8192)

s.recvfrom(8192)
