import socket
import sys
import time
import os
import re

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    # Send data
    #message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    filename = 'D:/Kuliah/Semester 4/Sistem Terdistribusi/FP/Tugas4/test.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       sock.send(l)
       #print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print >>sys.stderr, 'closing socket'
    sock.close
