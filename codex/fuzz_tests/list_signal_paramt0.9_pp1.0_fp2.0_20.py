import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        # just take the last value as it's good enough
        signal.setitimer(signal.ITIMER_REAL, delays[-1])

    print(signum, frame)

signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGVTALRM, handler)

for s in ('REAL', 'VIRTUAL'):
    signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    signal.setitimer(signal.ITIMER_VIRTUAL, delays.pop(0))
    print('.' * 20)
    for i in range(N):
        pass
