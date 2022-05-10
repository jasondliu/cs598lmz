import signal
# Test signal.setitimer() with SIGVTALRM

import os
import time
import sys
import signal

def handler(signum, frame):
    print('handler')
    sys.exit(0)

signal.signal(signal.SIGVTALRM, handler)

signal.setitimer(signal.ITIMER_VIRTUAL, 0.01, 0.01)

while True:
    pass
