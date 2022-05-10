import signal
# Test signal.setitimer
#setitimer(which, seconds, interval = 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 1)

for i in range(10):
    time.sleep(1)
    print('No signal so far')

signal.setitimer(signal.ITIMER_REAL, 1, 1)
for i in range(10):
    time.sleep(1)
    print('No signal so far')

signal.setitimer(signal.ITIMER_PROF, 1, 1)
for i in range(10):
    time.sleep(1)
    print('No signal so far')

import sys
def handler(signum, frame):
    print('Handler (%s,%s)' % (signum, frame))

signal.signal(signal.SIGVTALRM, handler)
signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGPROF, handler)

try:
    signal.setitimer(sign
