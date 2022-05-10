import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        sys.exit()

signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    time.sleep(1)
</code>
If you're just trying to measure time, then you might be better off using <code>time.time()</code>, as most OS's have a clock resolution of <code>1/100</code> of a second, so unless you're on a very high-end system you're not going to be able to get anything better than <code>10ms</code> resolution.

