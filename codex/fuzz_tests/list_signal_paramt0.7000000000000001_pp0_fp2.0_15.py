import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("\b." * N, end="")
        signal.setitimer(signal.ITIMER_REAL, 0)
    print("\b*", end="")

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0)

while 1:
    pass
