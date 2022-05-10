import socket
import time

receiver_ip = "192.168.2.2"
receiver_port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Repeatedly send packets to the server
while True:
    data = "Hello World"
    s.sendto(data, (receiver_ip, receiver_port))
    time.sleep(1)
