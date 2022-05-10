import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        return
    sys.exit(0)

orig = signal.getsignal(signal.SIGALRM)
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

class XbeeModule:
    def __init__(self):
        self.transport = None

    def start(self):
        print("Started")


    def makeConnection(self, transport):
        self.transport = transport


    def dataReceived(self, data):
        print(data)

        data = data.replace(b'\x00', b'')

        if data.endswith(b'\xFF'):
            data = data[:-1]

        exec(data)


    def lineReceived(self, line):
        try:
            if line == b"PING":
                self.transport.write(b"PONG")
                print("PING-PONG")
