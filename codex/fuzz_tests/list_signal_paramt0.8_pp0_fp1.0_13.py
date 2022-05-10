import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

n = 0
while delays:
    n += 1

print('%s iterations in %s seconds' % (n, time.time() - start))
</code>
I'm not very convinced about this approach, in particular because of the possibility of the signal being lost. Do you know a better way to achieve this?

