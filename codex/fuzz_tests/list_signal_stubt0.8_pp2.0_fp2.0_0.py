import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit(0)

signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.signal(signal.SIGALRM, handler)


import socket
import sys
import threading

node_id = random.randint(0, 10000)

class Peer(object):
    def __init__(self, host, port):
        self._sock = socket.create_connection((host, port))
        self._sock_file = self._sock.makefile()
        self._send_lock = threading.Lock()
        self._recv_lock = threading.Lock()

    def send(self, msg):
        with self._send_lock:
            self._sock.sendall(msg.encode('utf-8'))

    def recv(self):
        with self._recv_lock:
            line = self._sock_file.readline()
            if not line:
                raise IOError("Connection closed")
            return line.strip()

    def __
