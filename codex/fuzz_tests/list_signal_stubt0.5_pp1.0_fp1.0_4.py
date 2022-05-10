import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
</code>
This works, but I'm not sure whether it's the right way to do it. I have a few questions:

Is it OK to use <code>signal.setitimer</code> in this way?
Is it OK to use <code>signal.pause</code> in this way?
Is there a better way to do this?



A:

If you are using Python 3.3 or newer, the <code>signal.setitimer</code> function is available.
<code>import random
import signal
import time

def handler(signum=None, frame=None):
    print(signum, frame)

def main():
    N = 10000
    delays = [1e-6 + random.random() * 2e-5 for i in range(N)]
    signal.signal(signal.SIGALRM, handler
