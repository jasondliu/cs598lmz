import socket
import sys
import time

from datetime import datetime

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
# server_address = ('localhost', 10000)
server_address = ('169.254.137.65', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    for i in range(1, 100000):
        sock.sendall(str(i)+ " from " + str(datetime.now()) + "\n")
        time.sleep(1)
        data = sock.recv(1024)
        # print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr,
