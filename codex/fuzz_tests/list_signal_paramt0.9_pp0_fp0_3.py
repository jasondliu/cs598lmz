import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
        if delays:
            print('timer woke up with', delays[-1], 'left')

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, random.choice(delays))
print('first timer was set to', delays[-1], ' from the head of the list')
while delays:
    signal.pause()
