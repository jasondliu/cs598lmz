import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print('Done after %d iterations' % (N - len(delays)))
        sys.exit()

signal.signal(signal.ITIMER_REAL, handler)
signal.setitimer(signal.ITIMER_REAL, 1e-6)
print('Running %d iterations' % N)

while delays:
    pass
