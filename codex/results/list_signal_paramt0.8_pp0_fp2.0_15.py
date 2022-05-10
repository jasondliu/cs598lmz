import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    pass

print 'Done.'
</code>
Python 2.7.2 on Mac OS 10.7 results in the assertion error. I get the same error with Python 3.2.2.
Any idea why this error occurs or how I can fix it?
Thanks!
EDIT: Something is definitely wrong in the way that Python handles signals on Mac OS 10.7. Here's a more minimal example that also causes the same assertion error:
<code>import signal

signal.signal(signal.SIGALRM, lambda x,y: True)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)

while True:
    pass
</code>


A:

The <
