import socket
import struct
import sys

# Source IP, source port, dest IP, dest port, seq, ack seq
def checksum(msg):
    s = 0
    for i in range(0, len(msg), 2):
        w = ord(msg[i]) + (ord(msg[i+1]) << 8 )
        s = s + w
     
    s = (s>>16) + (s & 0xffff);
    s = s + (s >> 16);
     
    #complement and mask to 4 byte short
    s = ~s & 0xffff
     
    return s

def sniffer(sock, ifname):
    while True:
        packet = sock.recvfrom(2048)[0]
        packet = packet[0:20]
        ip = ".".join(str(ord(packet[i])) for i in range(12, 16))
        ip = ip + ":" + str(struct.unpack("!H", packet[20:22])[0])
        print ip

if __name__ == "__main__
