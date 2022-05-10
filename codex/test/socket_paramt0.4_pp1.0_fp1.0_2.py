import socket
socket.if_indextoname(3)

sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))

sock.bind(('eth0', 0))

#sock.bind(('enp0s3', 0))

while True:
    packet = sock.recvfrom(65565)
    print(packet)
