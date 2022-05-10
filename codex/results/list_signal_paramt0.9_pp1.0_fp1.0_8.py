import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
        signal.signal(signal.SIGALRM, handler)
    else:
        # reset to normal
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

signal.signal(signal.SIGALRM, handler)
print("Setting timer")
signal.setitimer(signal.ITIMER_REAL, delays.pop(0), 0)
print("Timer set")

while delays:
    signal.pause()
