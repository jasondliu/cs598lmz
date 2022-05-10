import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    print('SIGALRM')

signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.signal(signal.SIGALRM, handler)

import select
while delays:
    # select(rlist, wlist, xlist[, timeout])
    select.select([], [], [], 1.0)
</code>
It seems like there's an upper limit of 100 ms between signals.  On my machine, there's a ~10 ms delay between subsequent signals.  (So for my example, <code>N</code> should be 10.)

More info: As @Vince suggests in the comments, this might be a Linux kernel issue, and not Python.

