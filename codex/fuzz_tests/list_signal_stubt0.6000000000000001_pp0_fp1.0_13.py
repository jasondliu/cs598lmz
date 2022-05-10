import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
    print 'Signal handler called with signal', signum

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    signal.pause()
</code>


A:

You can use the <code>signal.setitimer</code> function. 
<code>&gt;&gt;&gt; import signal
&gt;&gt;&gt; signal.setitimer(signal.ITIMER_REAL, 0.1)
</code>

