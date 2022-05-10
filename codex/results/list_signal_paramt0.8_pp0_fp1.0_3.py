import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

while delays:
    signal.pause()
</code>
<code>SIGALRM</code> does not block its handler.  Instead, if you call <code>signal.pause()</code> in that handler, it simply suspends the process until you next receive a signal.  That signal will wake up the process, run the handler and then resume the <code>pause()</code>.
If you wanted more fine-grained control than that, you could use the <code>select</code> module to set a timeout whenever you want to delay, but that's a whole different approach.

