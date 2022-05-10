import socket
import os
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Send data
    filename = "kirim.txt"
    f = open(filename, 'rb')
    l = f.read(1024)
    while (l):
        sock.send(l)
        l = f.read(1024)
    f.close()
    print("Sending Done")
    sock.shutdown(socket.SHUT_WR)
    print("Receiving...")
    filename = "terima.txt"
    f = open(filename, 'wb')
    l = sock.recv(1024)
    while (l):
        f.write(l)
        l = sock.recv(1024)
    f.close()
