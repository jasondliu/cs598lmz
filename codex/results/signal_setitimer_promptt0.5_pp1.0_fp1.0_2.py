import signal
# Test signal.setitimer

import time

def handler(signum, frame):
    print 'handler called'

signal.signal(signal.ITIMER_REAL, handler)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(1)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(1)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(1)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(1)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(1)
signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
time.sleep(1)
signal.setitimer(signal.ITIMER_REAL
