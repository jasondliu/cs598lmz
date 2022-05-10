import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def sleep():
    # I can't find a better way without a decorator
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    while delays:
        signal.sigwaitinfo(signal.ITIMER_REAL)
</code>
It always works, but if <code>N</code> is small, the processes takes a long time to start sleeping (something like 100us). If <code>N</code> is big, the sleep precision is around 100us too.


A:

The first thing that comes to my mind is to get rid of the inner loop:
<code>def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

def sleep():
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    signal.sigwaitinfo(signal.ITIMER_RE
