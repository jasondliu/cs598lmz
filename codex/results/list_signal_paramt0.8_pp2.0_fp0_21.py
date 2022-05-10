import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        print("Timer finished")

signal.signal(signal.SIGALRM, handler)
handler()

class sock:
    def __init__(self, sock):
        self.socket = sock

    def recv(self, bufsize):
        return self.socket.recv(bufsize)

    def send(self, msg):
        return self.socket.send(msg)

    def shutdown(self):
        return self.socket.shutdown(socket.SHUT_RDWR)

    def close(self):
        return self.socket.close()

class myServer:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("localhost", 50000))
    s.listen(5)
    def __init__(self, sock = s):
        self.sock = sock
