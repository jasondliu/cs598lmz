import socket
socket.if_indextoname(6)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 53))

while True:
    (data, addr) = s.recvfrom(8192)
    print addr, len(data)
    domain = data[12:12+ord(data[11])]
    print domain
