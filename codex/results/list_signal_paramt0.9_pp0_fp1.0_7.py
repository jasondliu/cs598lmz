import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print delays
    else:
        print "done"

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while True:
    time.sleep(1)
</code>
This gives the following: <code>Traceback (most recent call last): ... KeyboardInterrupt</code>.
If you comment out the calls to setitimer (I used a # in front of each one), you get the desired result.
Any ideas?
EDIT: To be clear, I am interested in code that will timeout in 10 seconds or less.


A:

The problem is that the timeout clock is reset whenever a new timer is set (see sourcecode here). This is not explicitly mentioned in the documentation, but it's in the rationale.
A simple workaround is to use exponentially increasing timeouts, as shown below.
<code>import time
import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2
