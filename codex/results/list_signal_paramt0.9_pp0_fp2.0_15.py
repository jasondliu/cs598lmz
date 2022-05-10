import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    return True

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

from my_package import stuff
print stuff()

# == Results ==
# 1e-05
</code>
Basically, <code>my_package/stuff.py</code> has an assignment to <code>time.time</code> which gets delayed by the timer, which shows up in a different execution stack.
What do you think about this approach?
Environment info: Python 2.7 on GNU/Linux, but Windows and Python 3 would be nice too.
Cross-platform solution
Alright, thanks to the ihook event hook suggested by hpasteur, I got it working with Python 2.5 to 3.1, with the only exception being 2.5 and 2.6 on Windows. On Windows, you need to use <code>SetTimer</code> from <code>win32api</code> instead of <code>setitimer</code> and <code>signal
