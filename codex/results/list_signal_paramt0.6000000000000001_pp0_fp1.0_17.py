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

The following code seems to work correctly on my machine:
<code>import time
import random

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def wait():
    start = time.clock()

    while True:
        if time.clock() - start &gt;= delays[0]:
            break

        try:
            time.sleep(delays[0] / 2)
        except IOError:
            pass

    delays.pop(0)

while delays:
    wait()
</code>
However, as you can see, it is still polling, and it is not as accurate
