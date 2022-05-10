import signal
# Test signal.setitimer

import time

def handler(signum, frame):
    print "got alarm"

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 1.0, 0.5)

# Sleep for a while, and hope we get an alarm
time.sleep(3.0)

# Disable the timer
signal.setitimer(signal.ITIMER_REAL, 0)

print "done"
