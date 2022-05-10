import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    print('signal')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

print('bla')

while delays:
    t = 0
    while t < 1e-3:
        t1 = time.time()
        t2 = time.time()
        t = t2 - t1

print('bla')
