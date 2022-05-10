import socket
socket.if_indextoname(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('192.168.1.1', 5000))
s.recvfrom(1024)
