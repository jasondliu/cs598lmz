import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

while delays:
    pass
</code>
If you actually do want to emulate a timer, here's something that might work, though I didn't try it:
<code>import random
import time

N = 1000000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

try:
    last_tick = time.time()
    for delay in delays:
        time.sleep(delay - time.time() + last_tick)
        last_tick += delay

    print "All done."
except KeyboardInterrupt:
    print "Exiting"
</code>
This isn't as precise as with <code>signal.setitimer</code> of course; you still have to wait for the <code>time.sleep</code> to finish.

