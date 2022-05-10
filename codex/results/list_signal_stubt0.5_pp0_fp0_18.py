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
This code works fine, but if I change the <code>signal.ITIMER_REAL</code> to <code>signal.ITIMER_VIRTUAL</code> or <code>signal.ITIMER_PROF</code>, it doesn't work.
I guess that the <code>signal.ITIMER_VIRTUAL</code> and <code>signal.ITIMER_PROF</code> are not working in user space.
Is there a way to make <code>signal.ITIMER_VIRTUAL</code> or <code>signal.ITIMER_PROF</code> work in user space?


A:

You can't use <code>ITIMER_VIRTUAL</code> or <
