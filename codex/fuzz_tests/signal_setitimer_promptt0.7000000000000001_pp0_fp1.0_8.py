import signal
# Test signal.setitimer

import signal
import time

def handler(signum, frame):
    print "signal", signum

# signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# signal.setitimer(signal.ITIMER_REAL, 1, 1)
signal.setitimer(signal.ITIMER_VIRTUAL, 1, 1)
signal.signal(signal.SIGVTALRM, handler)
while True:
    time.sleep(1)

print "done"
