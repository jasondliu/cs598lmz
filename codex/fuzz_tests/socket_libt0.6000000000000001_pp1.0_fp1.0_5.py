import socket
import sys
import time
import threading
#import signal
#import curses
import os
import Queue

import signal
import sys
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


#server_address = ('localhost', 10000)
#sock.connect(server_address)

#sock.connect(('localhost', 10000))
#sock.connect(('192.168.1.1', 10000))

def send_tcp(host, port, message):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (host, port)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)

    try:
        
        # Send data
        print >>sys
