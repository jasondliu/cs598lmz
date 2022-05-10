import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

from timeit import Timer
from contextlib import contextmanager

@contextmanager
def timer():
    t0 = time.time()
    yield
    print('Elapsed time: {:.2f}s'.format(time.time() - t0))

with timer():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, delays.pop())
    while delays:
        signal.pause()


with timer():
    for delay in delays:
        handler(None, None)
