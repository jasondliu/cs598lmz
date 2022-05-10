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
    time.sleep(1)
</code>
This works fine, but the Python process consumes 100% of the CPU. I thought that using signals would avoid this, but apparently not.
What's the best way to do this in Python?


A:

In general, you can't do this with a single Python process. Python's main thread is busy in its event loop. You need a separate thread that blocks on the <code>sleep</code> call.

