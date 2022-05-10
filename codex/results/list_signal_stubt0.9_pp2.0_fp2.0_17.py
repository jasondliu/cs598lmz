import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)



timer = signal.itimer(signal.ITIMER_REAL, delays.pop(), 0)
signal.signal(signal.SIGALRM, handler)

</code>
I get the following message: 
<code>  Traceback (most recent call last):
  File "timer.py", line 24, in &lt;module&gt;
    timer = signal.itimer(signal.ITIMER_REAL, delays.pop(), 0)
AttributeError: '_timer' object has no attribute 'itimer'

</code>
Here is the python documentation: https://docs.python.org/3/library/signal.html#signal.itimer
What am I missing?

