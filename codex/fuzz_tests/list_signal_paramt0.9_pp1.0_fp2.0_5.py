import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0.0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(), 0.0)

start = time.time()
trapped = 0
for i in range(N):
    time.sleep(1.0)
    trapped += 1

print('Trapped {} signals in {} seconds'.format(trapped, time.time() - start))
