import socket
socket.if_indextoname(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("",12345))

while True:
    data, addr = s.recvfrom(1024)
