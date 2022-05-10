import socket
import sys
import json
import time

# get the host name
host = socket.gethostname()
port = 9999

# create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))

f = open("log.txt", "a+")

while True:
    print("Server is running...")
    data, addr = server.recvfrom(1024)
    f.write("\nClient {}: {}".format(addr, data.decode()))
    f.flush()
    # print("Client {}: {}".format(addr, data.decode()))
    server.sendto("Thanks for connecting me!".encode(), addr)

server.close()
