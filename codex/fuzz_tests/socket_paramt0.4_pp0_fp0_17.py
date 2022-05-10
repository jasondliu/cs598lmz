import socket
socket.if_indextoname(socket.if_nametoindex('lo'))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 6666))

while True:
    data, addr = s.recvfrom(1024)
    print(data.decode('utf-8'))
