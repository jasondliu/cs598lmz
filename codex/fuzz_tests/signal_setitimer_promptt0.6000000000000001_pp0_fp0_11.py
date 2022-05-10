import signal
# Test signal.setitimer()
#
# Test that the signal module has a setitimer() function.

import os
import signal
import time
import sys

if sys.platform[:3] in ('win', 'os2'):
    print('Warning: signal.setitimer() not supported on this platform')
    sys.exit(0)

def handler(signum, frame):
    if signum == signal.SIGALRM:
        print('SIGALRM received')
    else:
        print('SIGVTALRM received')

signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGVTALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1)
print('Sleeping for 1 second')
time.sleep(1)
print('Setting both timers to 0.5')
signal.setitimer(signal.ITIMER_REAL, 0.5)
