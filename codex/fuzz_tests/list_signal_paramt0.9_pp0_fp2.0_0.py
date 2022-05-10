import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_VIRTUAL, delays.pop(-1))
    else:
        signal.setitimer(signal.ITIMER_VIRTUAL, 0)

signal.signal(signal.SIGVTALRM, handler)
signal.setitimer(signal.ITIMER_VIRTUAL, delays.pop(-1))
while delays:
    signal.pause()
