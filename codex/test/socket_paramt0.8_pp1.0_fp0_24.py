import socket
socket.if_indextoname("11")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9728))

size = 10240
data = 'x' * size * 2

while True:
    s.send(data)
    print(s.recv(size*2))
