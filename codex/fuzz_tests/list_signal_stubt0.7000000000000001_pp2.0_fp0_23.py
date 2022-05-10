import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        for i in range(4):
            print(i)
        sys.exit()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())
</code>


A:

I have fixed your code, you have to use <code>signal.signal(signal.SIGALRM, handler)</code> instead of <code>signal.setitimer(signal.ITIMER_REAL, delays.pop())</code> in the else block:
<code>import sys
import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        for i in range(4):
            print(i)
        sys.exit()

signal.sign
