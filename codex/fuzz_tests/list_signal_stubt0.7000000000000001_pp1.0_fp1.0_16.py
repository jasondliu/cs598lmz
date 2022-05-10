import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
</code>
EDIT:
Here's a version that uses a single timer, and checks the current time every time it expires to see if the next timer has expired.  This should be more accurate than the above version.
<code>import time
import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays[0])

signal.signal(signal.SIGALRM, handler)

next_time = time.time()
while delays:
    now = time.time()
    while delays and next_time &lt;= now:
        print time.time() - next_time
        next_time += delays.
