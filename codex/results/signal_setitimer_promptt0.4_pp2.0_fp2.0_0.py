import signal
# Test signal.setitimer()

import sys
import time

def handler(signum, frame):
    print "Got signal", signum
    if signum == signal.SIGALRM:
        print "SIGALRM"
    elif signum == signal.SIGVTALRM:
        print "SIGVTALRM"
    else:
        print "Unknown signal"

signal.signal(signal.SIGALRM, handler)
signal.signal(signal.SIGVTALRM, handler)

# try to set an alarm for 1 second from now
signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)

# wait a bit
time.sleep(2)

# try to set an alarm for 1 second from now
signal.setitimer(signal.ITIMER_REAL, 1, 0)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 0)

# wait a bit
