import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("Done.")
        signal.setitimer(signal.ITIMER_REAL, 0)

print("Setting up timer...")
signal.signal(signal.SIGALRM, handler)
handler()

import time
time.sleep(5)

# Setting up timer...
# Done.
</code>

