import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

# init
signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGINT, lambda signum, frame: sys.exit(1))

handler()
while True:
    signal.pause()
