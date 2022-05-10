import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, delays.pop())

try:
    while delays:
        time.sleep(1)
except KeyboardInterrupt:
    pass
</code>


A:

It's probably because you're using timerfd on your new machine, but are calling <code>signal</code> functions.
The timerfd functions don't interact with the signal functions at all, they work completely differently.

