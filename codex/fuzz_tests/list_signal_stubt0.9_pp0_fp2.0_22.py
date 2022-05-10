import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("Done!")
        signal.setitimer(signal.ITIMER_REAL, 0)

# Register the signal function handler
signal.signal(signal.SIGALRM, handler)

# Kick off the first timer
signal.setitimer(signal.ITIMER_REAL, delays.pop())

# Wait 
while delays:
    signal.pause()
