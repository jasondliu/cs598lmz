import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, min(delays))
        delays.pop(0)
    else:
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, min(delays))

try:
    while delays:
        time.sleep(1)
except KeyboardInterrupt:
    pass

signal.setitimer(signal.ITIMER_REAL, 0)
</code>
I've found that <code>signal.setitimer(signal.ITIMER_REAL, min(delays))</code> is necessary for the first call to handler, but I'd like to be sure that it won't hurt.
Thanks in advance,

