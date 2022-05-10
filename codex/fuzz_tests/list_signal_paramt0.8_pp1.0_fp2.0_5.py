import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0), 0)

signal.signal(signal.SIGALRM, handler)

handler()

while delays:
    time.sleep(0.1)
</code>
However, I am uncertain if the time.sleep() is really necessary.  Could this code be rewritten without the time.sleep call?


A:

<code>SIGALRM</code> is typically delivered to the entire thread group, and therefore should wake up the thread group in the same way that any other signal that wakes up a signal handler would wake up the thread group.
However, this "wake up the thread group" signal behavior is only guaranteed by POSIX on signals that have the SA_RESTART flag set, and <code>SIGALRM</code> is not required to have this flag set (nor is it required to not have the flag set).  The man page for sigaction(2) says:
<blockquote>
<p>By default, most signals cause signal-catching functions to be restarted after they are interrupted by signals (see longjmp(3)). 
