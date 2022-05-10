import socket
socket.if_indextoname(3)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 40000))

while True:
    data = sock.recv(65535)
    print(data)
