import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop(0))
    else:
        sys.exit()

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

x = 0
while True:
    x += 1

# Test case for LazySignal.

import time
import signal

def handler(signum, frame):
    print "Signal handler called with signal", signum

h = signal.signal(signal.SIGUSR1, handler)

print "Before lazy:", h
h.lazy = True
print "After lazy:", h

print "Sending first signal"
os.kill(os.getpid(), signal.SIGUSR1)
time.sleep(2)
