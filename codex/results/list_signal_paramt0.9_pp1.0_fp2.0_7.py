import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_PROF, delays.pop(), 0)
        print("Timer expired")
    else:
        sys.exit(0)

signal.signal(signal.SIGPROF, handler)
signal.setitimer(signal.ITIMER_PROF,  delays.pop(0), 0)

while True:
    signal.pause()
