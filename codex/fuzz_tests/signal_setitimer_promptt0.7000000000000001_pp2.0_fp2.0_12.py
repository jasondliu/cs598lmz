import signal
# Test signal.setitimer and signal.getitimer

import errno
import sys
import time

alarm_time = min(max(0.03, sys.getcheckinterval() / 50), 0.1)

def handler(signum, frame):
    global alarm_time
    if signum == signal.SIGALRM:
        print('SIGALRM received')
        alarm_time *= 2
        signal.setitimer(signal.ITIMER_REAL, alarm_time, 0)
    elif signum == signal.SIGVTALRM:
        print('SIGVTALRM received')
    else:
        print('signal %d received' % signum)

signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGVTALRM, handler)

itimer_vals = []
for i in range(10):
    time.sleep(1)
    itimer_vals.append(signal.getitimer(signal.ITIMER_REAL))
    itimer_vals.append(
