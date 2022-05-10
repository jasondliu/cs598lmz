import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while delays:
    time.sleep(1)
</code>
The above code has the following issues:

The time between the timer being set and the signal being delivered is not guaranteed to be exactly the time specified in the <code>setitimer</code> call.  This is due to how the signal is delivered, and is not specific to Python.
The signal handler is not re-entrant.  If the signal handler is still running when another signal is delivered, the second signal will be lost.  This is due to how the signal is delivered, and is not specific to Python.
The signal handler is not interruptible.  If the signal handler is running when another signal is delivered, the signal will not be delivered until the signal handler returns.  This is due to how the signal is delivered, and is not specific to Python.

To solve the first issue, we
