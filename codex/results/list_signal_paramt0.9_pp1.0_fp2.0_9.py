import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, 0.1)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1)

sys.stdout.write("Started ...\n")
while delays:
    sys.stdout.write("===========\n")
    time.sleep(delays.pop(0))
    sys.stdout.write("===========\n")
</code>
Output:
<code>Started ...
===========
===========
===========
===========
===========
===========
========...
</code>

Even if you need to continue the sleep even if the signal arrives, it can be handled via the same way - by just removing the signal handler.
<code>N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    global delays
    if delays:
        signal.setitimer(signal.ITIMER
