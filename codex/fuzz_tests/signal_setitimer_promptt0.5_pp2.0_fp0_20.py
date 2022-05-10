import signal
# Test signal.setitimer() and signal.getitimer()

import os
import sys
import time
import signal

def alarm_handler(signum, frame):
    print 'Alarm!'

signal.signal(signal.SIGALRM, alarm_handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

for i in range(5):
    print 'Sleeping for %d sec' % i
    time.sleep(1)

signal.setitimer(signal.ITIMER_REAL, 0)
print 'Done'
