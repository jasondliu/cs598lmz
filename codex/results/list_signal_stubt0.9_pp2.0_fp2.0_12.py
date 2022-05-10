import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print 'done'

## signal.signal(signal.SIGALRM, handler)
## signal.setitimer(signal.ITIMER_REAL, delays.pop())
## signal.pause()

import signal, os

def handler(signum, frame):
  print "pid ", os.getpid(), " received signal ", signum

signal.signal(signal.SIGTERM, handler)
print os.getpid()

while True:
  signal.pause()
