import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print('Timers done')
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
handler()

while delays:
    signal.pause()
</code>
This runs for about 100 seconds on my machine (with Python 3.3.3), and it does not take up all the CPU time.

