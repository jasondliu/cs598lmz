import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, min(delays), min(delays))
    return True
signal.setitimer(signal.ITIMER_REAL, min(delays), min(delays))
signal.signal(signal.SIGALRM, handler)

while delays:
    delays.pop(0)
