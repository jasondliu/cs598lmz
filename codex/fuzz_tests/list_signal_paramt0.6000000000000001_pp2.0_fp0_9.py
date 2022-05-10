import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

try:
    while delays:
        time.sleep(1)
except KeyboardInterrupt:
    print('\n\nBye!')

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
