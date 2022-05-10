import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
</code>
I've tried the following:

Using <code>signal.setitimer</code> with <code>signal.ITIMER_REAL</code> and <code>signal.ITIMER_VIRTUAL</code>
Using <code>signal.setitimer</code> with <code>signal.ITIMER_REAL</code> and <code>signal.ITIMER_PROF</code>
Using <code>signal.setitimer</code> with <code>signal.ITIMER_REAL</code> and <code>signal.ITIMER_REAL</code>
Using <code>signal.setitimer</code> with <code>signal.ITIMER_REAL</code
