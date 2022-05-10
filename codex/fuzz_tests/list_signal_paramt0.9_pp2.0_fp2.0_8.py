import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, 0)
        delays.sort()
        delay = delays.pop()
        signal.setitimer(signal.ITIMER_REAL, delay)
        print('%s' % delay)
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
delay = delays.pop()
signal.setitimer(signal.ITIMER_REAL, delay)

while True:
    signal.pause()
