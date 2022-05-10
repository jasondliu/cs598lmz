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
handler()

while delays:
    signal.pause()
</code>
The only problem with this is that it doesn't take into account the time spent in <code>pause()</code> and <code>handler()</code>, so the actual delays will be longer than requested.
Edit:
To solve the problem of the delays being longer than requested, we can do this:
<code>import signal
import time

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    while delays:
        t = time.time()
        d = delays.pop()
        signal.setitimer(signal.ITIMER_REAL, d)
        time.sleep(d)
        if delays:
            dt = time.time() - t - d
            delays[-1] -=
