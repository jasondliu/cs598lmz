import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, 0)
        delays.pop()
        signal.setitimer(signal.ITIMER_REAL, delays[-1])
    else:
        print('done')
        signal.setitimer(signal.ITIMER_REAL, 0)

signal.setitimer(signal.ITIMER_REAL, delays[-1])
signal.signal(signal.SIGALRM, handler)

try:
    while True:
        pass
except KeyboardInterrupt:
    print('stopped')
</code>

