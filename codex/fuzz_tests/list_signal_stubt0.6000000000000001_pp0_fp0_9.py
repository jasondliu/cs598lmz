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
    time.sleep(1.0)

print 'DONE'
</code>
Unfortunately it does not work at all. I'm using Python 2.7 on Ubuntu 12.04. I also tested on Mac OS X with the same result.
What am I doing wrong?


A:

The problem is that <code>sleep</code> is a blocking call that causes the program to wait for a period of time.  This means that the <code>SIGALRM</code> signal (which is the signal that the timer sends) is queued up and not delivered to your program until the <code>sleep</code> call is executed.  Since your program is waiting in the <code>sleep</code> call, your timer handler is never invoked, so the timer is never set up again.
You can fix this problem by using <code>select.select</code> instead of <code>sleep</code>:
<code>import select

