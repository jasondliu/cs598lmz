import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

if delays:
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
</code>
It generates a list <code>delays</code> of 10,000 time intervals and schedules the first one. When the time interval is up, it schedules the next one.
If you want to do work, you can put that work in the handler.
A timer can be cancelled by passing <code>signal.setitimer(signal.ITIMER_REAL, 0)</code> and the handler will stop being called. You can use this to implement the <code>timeout</code> function.

