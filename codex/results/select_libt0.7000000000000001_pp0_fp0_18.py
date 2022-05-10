import select
import socket
import sys
import signal
import json

class Process:
    def __init__(self, config):
        self.config = config
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self.sock.connect(config['socket'])

    def __del__(self):
        self.sock.close()

    def run(self):
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        inp = self.config['in']
        outp = self.config['out']
        poller = select.poll()
        poller.register(inp, select.POLLIN)
        while True:
            ready = poller.poll()
            if ready:
                data = inp.readline()
                if not data:
                    break
                self.sock.send(data)
                data = self.sock.recv(2048)

