import socket
# Test socket.if_indextoname
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(0, 10000):
    sock.sendto("h", ("10.0.0.1", 0xffff))
    recv = sock.recvfrom(1024)
    if recv[0] != "h":
        print("Socket test failed")
        exit(1)

print("Socket test success")
