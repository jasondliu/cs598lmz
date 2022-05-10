import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
        sys.exit()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0)

while delays:
    handler()

# time python ./itimer.py
# python ./itimer.py  0.02s user 0.01s system 99% cpu 0.031 total
