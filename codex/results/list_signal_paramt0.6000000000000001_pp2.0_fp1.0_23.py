import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        print "Done."
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

while delays:
    signal.pause()
</code>
On my system, it takes about 20 seconds to run. When I kill it with CTRL-C, I get this message:
<code>^CTraceback (most recent call last):
  File "timer.py", line 23, in &lt;module&gt;
    signal.pause()
  File "/usr/lib64/python2.6/signal.py", line 47, in pause
    return _pause()
KeyboardInterrupt
</code>
I don't understand why it's not returning from <code>signal.pause()</code>. What am I doing wrong?


A:

The <code>signal.pause()</code>
