import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, 0)
        next = delays.pop()
        signal.setitimer(signal.ITIMER_REAL, next)
        print '%d remain' % len(delays)
        return

    print 'Done'
    exit(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0)
signal.setitimer(signal.ITIMER_REAL, 1e-6)

while True:
    pass
