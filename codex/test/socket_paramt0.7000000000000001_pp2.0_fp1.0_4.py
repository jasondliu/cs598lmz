import socket
socket.if_indextoname(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 5555))
s.sendto(b'hello', ('192.168.20.7', 5555))
s.recv(1024)
s.sendto('hello', ('192.168.20.7', 5555))
s.recv(1024)
