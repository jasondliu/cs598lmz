import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print("Timer is now set to...", delays)
signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

input("Hit enter to stop...")
</code>


A:

I think that you should use <code>signal.setitimer</code> (<code>signal.setitimer()</code> and <code>signal.getitimer()</code> return a 3-tuple containing the number of seconds and microseconds before the timer expires, and the timer type).
<code>signal.setitimer(signal.ITIMER_REAL, 1e-6 + random.random() * 2e-5)
</code>

