import socket
socket.if_indextoname(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 0))
s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'eth0')
