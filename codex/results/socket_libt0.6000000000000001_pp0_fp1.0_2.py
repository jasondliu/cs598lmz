import socket
import sys
import time

def send(sock, message):
    print("Sending {0}".format(message))
    sock.sendall(message)


def receive(sock):
    data = sock.recv(1024)
    print("Received {0}".format(data))


def send_and_receive(sock, message):
    send(sock, message)
    receive(sock)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {0} port {1}'.format(*server_address))
sock.connect(server_address)

try:
    send_and_receive(sock, "Hello world 1".encode())
    send_and_receive(sock, "Hello world 2".encode())
    send_and_receive(sock, "Hello world 3".encode())
   
