import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

import time
time.sleep(100)
</code>
When I run it, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 14, in &lt;module&gt;
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
ValueError: interval must be positive
</code>
It looks like the <code>delays.pop()</code> call is returning zero, but I can't figure out why.
Can anyone explain what's going on here?


A:

The <code>itimer</code> call is being called twice.  Once when you call it, and once when the signal is raised.  It fails on the signal.  The simplest way to fix this is to move the <code>delays.pop</code> call into the signal handler.  That way, it will only be called when a signal is
