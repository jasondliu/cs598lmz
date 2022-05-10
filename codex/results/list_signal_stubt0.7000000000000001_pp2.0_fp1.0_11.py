import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
signal.signal(signal.SIGALRM, handler)

# go!
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
</code>
Which runs for about 1.2 seconds on my machine.

Now, the usual way to measure wallclock time is to use <code>time.time</code> and <code>time.clock</code>.  If we take the difference of the two and print it every <code>N</code> iterations, that gives you a rough idea of how much of the processing is done in user space, and how much is being done in kernel space -- and hence how much of your time is spent in "polling" vs. "handling".
<code>import signal
import time

N = 10000

def handler(signum=None, frame=None):
    pass
signal.signal(signal.SIGALRM, handler)

# go!
signal.setitimer(signal.ITIMER_REAL, 0.001)

for i
