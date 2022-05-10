import select
import time

class Collector(object):
    def __init__(self, path):
        self.path = path
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self.sock.bind(self.path)

    def run(self):
        while True:
            readable, _, _ = select.select([self.sock], [], [], 0.1)
            for s in readable:
                if s is self.sock:
                    data, _ = self.sock.recvfrom(1024)
