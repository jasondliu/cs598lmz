import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        signal.setitimer(signal.ITIMER_REAL, 0.0)

# SIGALRM is only usable on a select()able file descriptor
signal.signal(signal.SIGALRM, lambda signum, frame: None)

signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

while delays:
    try:
        signal.pause()
    except KeyboardInterrupt:
        break
    handler()
