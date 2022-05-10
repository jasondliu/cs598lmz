import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print "Time's up!"

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
print "All done."
</code>


A:

From the signal module documentation:
<blockquote>
<p>SIGALRM This signal is used to inform a process that the time limit specified by a prior call to the alarm() function has expired. SIGALRM is defined on all POSIX systems. Only one timer may be active at a time. An active timer can be reset by calling alarm() with a non-zero argument, and a pending timer will be canceled by a call with a value of 0.</p>
</blockquote>
If you set the signal to something else in the handler you'll get a recursion.

