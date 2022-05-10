import socket
socket.if_indextoname(2)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('10.255.255.255', 1))
s.getsockname()[0]
