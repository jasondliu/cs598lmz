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
    time.sleep(1)
</code>
I'm running this on a Debian VM with 8GB RAM and 4 cores. 
When I run this script with Python 2.7.9, the script runs without a hitch.
When I run this script with Python 3.4.2, the script throws a KeyboardInterrupt after a few seconds.
I'm wondering if there is a bug in the Python 3.4.2 signal handling or if there is something I'm missing.

