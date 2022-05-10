import socket
socket.if_indextoname(2)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 1234))
s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'eth0')

while True:
    print(s.recv(4096))
