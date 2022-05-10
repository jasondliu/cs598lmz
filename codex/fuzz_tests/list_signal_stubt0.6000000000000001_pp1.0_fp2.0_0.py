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
</code>
This does not work very well, though. I'm getting about 2% of missed signals. I then tried to test it with <code>itimer_settime</code>:
<code>import random
import signal
import time

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        delay = delays.pop()
    else:
        delay = 0
    signal.itimer_settime(signal.ITIMER_REAL, delay, 0)

signal.signal(signal.SIGALRM, handler)
signal.itimer_settime(signal.ITIMER_REAL, delays.pop(), 0)


