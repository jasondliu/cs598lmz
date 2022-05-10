import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(
            signal.ITIMER_REAL,
            delays.pop(0),
            0)

# schedule an event to wake us up in 2 seconds
signal.signal(signal.SIGALRM, handler)
signal.setitimer(
    signal.ITIMER_REAL,
    delays.pop(0),
    0)

old_handler = signal.signal(signal.SIGALRM, handler)

# wait for events
while delays:
    signal.pause()
