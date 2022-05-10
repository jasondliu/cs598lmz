import socket
import sys
import os
import base64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
host = '127.0.0.1'
port = 8888
server_address = (host, port)

print(f"connecting to {host}:{port}")
sock.connect(server_address)

#file
filename = input("Input file name : ")
if os.path.isfile(filename):
    f = open(filename,'rb')
    k = f.read()
    f.close()
    k=base64.b64encode(k)
    print("Sending...")
    sock.send(k)
    print("Sent!")
else:
    print("file not found")

#closing connection
sock.close()
