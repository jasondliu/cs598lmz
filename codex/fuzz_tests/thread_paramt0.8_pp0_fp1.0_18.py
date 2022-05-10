import sys, threading
threading.Thread(target=lambda: sys.stdout.write("thread 1\n")).start()
threading.Thread(target=lambda: sys.stdout.write("thread 2\n")).start()
sys.stdout.write("main thread\n")

# Python provides two levels of access to network services.
# Low-level access to network protocols.
# A high-level interface that makes it easy to use client and server applications.
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
#mysock.close()

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break

