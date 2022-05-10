import socket
socket.if_indextoname(1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 1234))

while True:
    msg, addr = s.recvfrom(1024)
    print("got %s from %s" % (msg, addr))
    s.sendto("got it".encode("utf-8"), addr)
