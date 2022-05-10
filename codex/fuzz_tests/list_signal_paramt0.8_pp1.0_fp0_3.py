import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        print("done the iteration")

def foo():
    global N
    for i in range(N):
        pass

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop(0))

foo()
print("done processing")
