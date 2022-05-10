import socket
socket.if_indextoname(1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 60000))

while True:
    msg, address = s.recvfrom(1024)
    print(msg)
