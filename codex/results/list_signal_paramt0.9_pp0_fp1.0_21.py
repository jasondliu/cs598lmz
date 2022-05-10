import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit(0)

signal.setitimer(signal.ITIMER_REAL, random.random() * 0.001)
signal.signal(signal.SIGALRM, handler)

for i in xrange(N):
    print i
    time.sleep(delays.pop())
