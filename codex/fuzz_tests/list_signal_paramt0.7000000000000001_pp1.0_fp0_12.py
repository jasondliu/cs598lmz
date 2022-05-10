import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

for sig in [signal.SIGALRM, signal.SIGVTALRM, signal.SIGPROF]:
    print('%s: ' % sig, end=' ')
    signal.signal(sig, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    t1 = time.time()
    while delays:
        pass
    print(time.time() - t1)
