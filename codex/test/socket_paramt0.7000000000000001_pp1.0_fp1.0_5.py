import socket
socket.if_indextoname(1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 54321))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    data, addr = s.recvfrom(1024)
