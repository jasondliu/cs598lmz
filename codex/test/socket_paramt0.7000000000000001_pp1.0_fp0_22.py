import socket
socket.if_indextoname(int(r[0][0][17:]))

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
s.bind((socket.if_indextoname(int(r[0][0][17:])), 0))

# receive a packet
while True:
    packet = s.recv(1024)
    print(packet)
