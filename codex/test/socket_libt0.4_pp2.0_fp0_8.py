import socket
import threading
import time
import sys
import os

def send_file(filename):
    if os.path.isfile(filename):
        f = open(filename, 'rb')
        packet = f.read(1024)
        while packet != '':
            s.send(packet)
            packet = f.read(1024)
        s.send('DONE')
        f.close()
    else:
        s.send('Unable to find out the file')

def recv_file(filename):
    f = open(filename, 'wb')
    i = 1
    while True:
        bits = s.recv(1024)
        if bits.endswith('DONE'):
            f.write(bits[:-4])
            f.close()
            break
