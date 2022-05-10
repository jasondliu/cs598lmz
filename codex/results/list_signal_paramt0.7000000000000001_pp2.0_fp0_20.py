import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0)
signal.signal(signal.SIGALRM, handler)

while delays:
    signal.pause()
    print('foo', end='')
print()
</code>
This code, however, prints nothing. It seems <code>signal.pause</code> must not be called from the signal handler. Why?
I read the documentation of <code>signal.pause</code> but it's too cryptic.


A:

From the signal module documentation:
<blockquote>
<p>Python signal handlers are always executed in the main Python thread, even if the signal was received in another thread. Python signal handlers are called with two arguments: the signal number and the current stack frame.</p>
</blockquote>
It's called with 2 arguments, so the <code>frame</code> argument is not <code>None</code>, and the <code>while</code> loop doesn't run, because <code>delays</code
