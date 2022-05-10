import selectors
import sys
import time

class TCPClient(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sel = selectors.DefaultSelector()

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.sock.setblocking(False)
        self.sel.register(self.sock, selectors.EVENT_READ, self.read)

    def read(self, sock, mask):
        data = sock.recv(1024)
        if data:
            print("received:", repr(data))
        else:
            print("closing connection to", sock.getpeername())
            self.sel.unregister(sock)
            sock.close()

    def run(self):
        self.start()
        while True:
            events = self.sel.select(timeout=1)
            for key, mask
