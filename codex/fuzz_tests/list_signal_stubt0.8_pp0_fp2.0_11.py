import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())

def loop(N):
    signal.signal(signal.SIGALRM, handler)  # Register handler
    handler()                               # Set alarm to go off in first delay
    while delays:
        # Notify me when real time has elapsed
        signal.pause()
        print(N - len(delays), end=' ')

loop(N)
