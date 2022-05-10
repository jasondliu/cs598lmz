import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0)

while delays:
    signal.pause()
</code>
The time to execute the code above is about 2.5 seconds on my machine. 
The time to execute the same code but with all delays set to zero is about 0.15 seconds.
My question is: 

Why is the time to execute the code so much longer when the delays are non-zero?
Is there a way to speed up the code when the delays are non-zero?

I have tried to use the <code>multiprocessing</code> module to run the code in parallel, but the speedup is only about 20% (i.e. from 2.5 seconds to 2 seconds).
I am running Python 3.5.1 on Ubuntu 16.04.

