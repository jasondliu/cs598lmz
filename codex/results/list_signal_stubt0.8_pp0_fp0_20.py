import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        return
    sys.exit()

signal.signal(signal.SIGALRM, handler)
handler()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 4444))
s.send(b'%c' % N)
s.close()
