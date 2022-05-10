import signal
# Test signal.setitimer
#
# Modified from:
#   https://docs.python.org/2/library/signal.html#signal.setitimer
#

import os
import signal
import time
import sys
import threading

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")

def check_timer():
    signal.signal(signal.SIGALRM, handler)

    for i in range(3):
        print 'Setting alarm'
        signal.setitimer(signal.ITIMER_REAL, 1)
        try:
            print 'Sleeping'
            time.sleep(3)
        except IOError, msg:
            print 'Got', msg
        else:
            print 'No alarm yet'
            time.sleep(0.5)

def check_timer_after():
    signal.signal(signal.SIGALRM, handler)

    for i in range(3):
        print 'Setting alarm'
        signal.setitimer(sign
