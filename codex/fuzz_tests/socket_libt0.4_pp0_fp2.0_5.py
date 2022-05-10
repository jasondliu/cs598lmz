import socket
import sys
import time
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    # Send data
    filename = input("Masukkan nama file yang ingin diupload : ")
    f = open(filename,'rb')
    k = f.read()
    sock.send(k)
    f.close()
    print("File berhasil diupload")

finally:
    print('closing socket')
    sock.close()
