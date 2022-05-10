import socket,sys
import struct
import time
import random

port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',port))

while True:
    message, address = s.recvfrom(1024)
    print(message.decode())
    s.sendto(b'ack', address)
