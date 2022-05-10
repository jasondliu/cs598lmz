import socket
import time
import sys
import threading

if len(sys.argv) < 2:
    print "Usage: python %s <port>" % sys.argv[0]
    exit(2)

class Server(threading.Thread):
    def __init__(self, sock, addr):
        threading.Thread.__init__(self)
        self.sock = sock
        self.addr = addr
        self.start()

    def run(self):
        for i in range(5):
            print "TCP server: %s %d" % self.addr
            time.sleep(1)
            self.sock.send("Hello, world")
        self.sock.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', int(sys.argv[1])))
s.listen(5)
while True:
    sock, addr = s
