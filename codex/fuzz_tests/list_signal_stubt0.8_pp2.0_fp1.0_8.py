import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def loop():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    while delays:
        signal.pause()

t = timeit.Timer('loop()', 'from __main__ import loop')
print '%.3fs' % t.timeit(1)
</code>
I think the blocking nature of the <code>pause</code> function is probably bad.
This version reduces the duration a bit, but it is not blocked, but it still uses a lot of CPU:
<code>import signal
import time
import timeit
import random

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum, frame):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def loop():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.
