import select
import socket

class SimpleHTTPServer(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((ip, port))
        self.server.listen(5)

    def start(self):
        inputs = [self.server, sys.stdin]
        running = True
        while running:
            try:
                readable, writable, exceptional = select.select(inputs, [], [])
                for s in readable:
                    if s is self.server:
                        self.on_accept()
                    elif s is sys.stdin:
                        junk = sys.stdin.readline()
                        running = False
            except KeyboardInterrupt:
                running = False
        self.server.close()

    def on_accept(self):

