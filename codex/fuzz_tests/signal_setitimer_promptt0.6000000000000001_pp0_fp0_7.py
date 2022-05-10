import signal
# Test signal.setitimer()
#
# This test is Linux-specific, because it uses the ITIMER_REAL
# timer, which Linux is the only OS to support.

import os
import signal
import time
import sys

# The signal handler for the timer

def handler(signum, frame):
    print "handler called"
    global hit
    hit = 1

# Set a timer

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.2, 0)

# Wait for it to go off

print "Waiting..."
sys.stdout.flush()
hit = 0
while not hit:
    time.sleep(0.1)

# Now cancel it

signal.setitimer(signal.ITIMER_REAL, 0)

# Wait for a bit to make sure it doesn't go off again

time.sleep(0.3)

# See if it went off again

if hit > 1:
    print "FAIL: handler called more than once!"
