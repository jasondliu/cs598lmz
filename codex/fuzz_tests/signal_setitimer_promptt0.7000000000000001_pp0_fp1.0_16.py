import signal
# Test signal.setitimer().
import os
import time

def handler(signum, frame):
    print 'Signal handler called with signal', signum

# Set the signal handler and a 5-second alarm
signal.setitimer(signal.ITIMER_REAL, 5)

signal.signal(signal.SIGALRM, handler)

# Do stuff
time.sleep(6)
print "Done!"
