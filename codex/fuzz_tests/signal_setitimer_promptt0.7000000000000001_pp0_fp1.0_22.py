import signal
# Test signal.setitimer and signal.setitimer.
# This is a test for SF bug #1046288.
#
# Without any changes, this script causes Python to crash with a "Segmentation
# fault" on Linux/x86.

import time
#import signal

def handler(signum, frame):
    print "timeout"
    print "FAIL"
    sys.exit(1)

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
time.sleep(1)
print "OK"
