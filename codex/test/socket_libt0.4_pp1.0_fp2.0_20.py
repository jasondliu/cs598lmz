import socket
import sys
import time
import threading
import os
import subprocess
import signal

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def handler(clientsocket, clientaddr):
    while True:
        data = clientsocket.recv(1024)
        if data:
            print('received {!r}'.format(data))
            clientsocket.sendall(data)
        else:
            print('no data from', clientaddr)
            break

while True:
    print('waiting for a connection')
    clientsocket, clientaddr = sock.accept()
    print('connection from', clientaddr)
    threading.Thread(target=handler, args=(clientsocket, clientaddr)).start()
