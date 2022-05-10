import socket



server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("", 8000))

while True:
    data, addr = server.recvfrom(1024)
    print("%s: %s" % (addr, data.decode("utf-8")))
    server.sendto(b"world", addr)
