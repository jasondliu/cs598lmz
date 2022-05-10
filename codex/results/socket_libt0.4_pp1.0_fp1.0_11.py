import socket
import struct
import sys
import time
import threading

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

def send_msg(msg):
    # Send data
    message = msg
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

def recv_msg():
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

def recv_msg_thread():
    while True:
        data = sock.recv(16)
