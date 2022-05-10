import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print('done')
        sys.exit(1)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, delays.pop())

while True: pass
</code>
Another variant (2)
But its more fun to spend 100ms every 10s and 1000ms every minute:
<code>import datetime
import signal
import sys

c = 0

def handler(signum=None, frame=None):
    global c
    c += 1
    if c % 600 == 0:
        print(datetime.datetime.now(), 'executing 100ms')
        signal.setitimer(signal.ITIMER_REAL, 0.1)
    elif c % 60 == 0:
        print(datetime.datetime.now(), 'executing 1000ms')
        signal.setitimer(signal.ITIMER_REAL, 1)
    else:
        print(datetime.datetime.now(), 'executing 0ms')
        sys
