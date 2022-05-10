import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
        return
    signal.setitimer(signal.ITIMER_REAL, 0)
    sys.exit()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1e-6)

while delays:
    pass
</code>
It is possible to write a more efficient version that minimizes the amount of busy waiting. However, unless you really really really really really really really need to do this, you should probably go for something like a <code>select()</code> loop instead. 

