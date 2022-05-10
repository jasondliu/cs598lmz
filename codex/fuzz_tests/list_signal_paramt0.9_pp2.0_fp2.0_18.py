import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)
        print("Done")

signal.signal(signal.SIGALRM, handler)
handler()
while delays:
    time.sleep(random.random() * 5e-2)
</code>
That is, the signal handler computes next time to wait, and then sets up the timer. The <code>time.sleep(...)</code> gives a chance to another thread to run.
If you use Python's high-level timer functions, they set timers on the main thread.

