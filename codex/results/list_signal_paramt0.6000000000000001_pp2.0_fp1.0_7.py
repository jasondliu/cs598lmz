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
        signal.signal(signal.SIGALRM, signal.SIG_DFL)
        print('done')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, min(delays))
</code>
I'm not sure if it's the best way, but it works.

