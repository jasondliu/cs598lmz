import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
handler()
signal.pause()
</code>


A:

By default <code>signal.pause()</code> causes the current
process to block, waiting for a signal.
While it is waiting, all signals that arrive will be
consumed, but not reported.
Before this behavior was discovered, I searched for another
way to block, and found the semaphore
(file descriptor) <code>/dev/initctl</code> will block:
<code>import time
import random
import signal
import os

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
handler()
# Blocking call to setitimer
