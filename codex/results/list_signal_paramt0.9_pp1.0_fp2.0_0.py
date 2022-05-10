import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

delay = delays.pop()
signal.signal(signal.ITIMER_REAL, handler)
signal.setitimer(signal.ITIMER_REAL, delay)
time.sleep(10)
</code>
Alternatively you could use <code>signal.pause</code> to return control to the signal handler:
<code>import signal
import time

# ...
signal.pause()
time.sleep(0)
</code>

