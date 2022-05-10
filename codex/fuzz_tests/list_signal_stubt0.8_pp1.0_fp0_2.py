import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    print('got it', sum(delays))
    # or do anything else that needs to be done

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1e-6 + delays.pop())

while delays:
    signal.pause()
</code>
The above works fine when I run it, but I wonder if there's a more efficient way?

