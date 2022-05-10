import signal
# Test signal.setitimer

import os
import signal
import time

def handler(signum, frame):
    print 'SIGALRM caught!'

def testit():
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.01)

print "Before sleeping"
testit()
time.sleep(1)
print "After sleeping"
