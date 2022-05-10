import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
        print(len(delays))
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0)
handler()

while delays:
    signal.pause()
</code>
However, this is not very accurate. For example, even with a delay of 1e-6 (1 us), the actual delay is often much longer.
Is there a way to make this more accurate?


A:

The problem is that <code>signal.pause()</code> is not very accurate. It's defined to return only when a signal is received or when a signal handler raises an exception. But it's not defined to return immediately after the signal is received.
If you want to sleep for a short amount of time, <code>time.sleep</code> is more accurate than <code>signal.pause</code>.
<code>import random
import signal
import time

N = 10000
delays = [1e-6
