import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

def wait():
    while delays:
        signal.pause()
# wait()

def handler(signum=None, frame=None):
    if delays:
        # seconds, microseconds
        signal.setitimer(signal.ITIMER_REAL, 0, delays.pop() * 1e6)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0, delays.pop() * 1e6)
wait()
