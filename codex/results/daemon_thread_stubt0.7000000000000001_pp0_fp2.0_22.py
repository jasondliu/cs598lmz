import sys, threading

def run():
    server = socket.socket()
    server.bind(('localhost', 65432))
    server.listen(5)
    client, address = server.accept()
    print 'Connected by', address
    while 1:
        client.send('Hello World')
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    while 1:
        time.sleep(1)

main()
</code>
And here is the client (not complete yet):
<code>import socket
import time
import threading

def run():
    server = socket.socket()
    server.connect(('localhost', 65432))
    while 1:
        print server.recv(1024)

def main():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    while 1:
        time.sleep(1)

main()
</code>


A:

In Python 3, the <code>
