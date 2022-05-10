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
Note that I had to increase the delays a bit to make sure that the <code>sleep</code> call didn't "steal" the first few timer signals, but other than that it looks perfectly okay to me.

