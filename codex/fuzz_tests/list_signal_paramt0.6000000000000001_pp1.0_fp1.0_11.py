import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

while delays:
    signal.pause()
</code>
And here's a version that uses <code>sched</code>:
<code>import sched
import time
import random

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(args=None):
    if delays:
        s.enter(delays.pop(0), 1, handler)

s = sched.scheduler(time.time, time.sleep)
s.enter(delays.pop(0), 1, handler)
s.run()
</code>
The <code>sched</code> solution is much closer to what you want.

