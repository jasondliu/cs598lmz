import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, min(delays[1:]), 0)
    del delays[0]

    if not delays:
        sys.exit(0)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, min(delays[1:]), 0)

while True:
    time.sleep(1)
