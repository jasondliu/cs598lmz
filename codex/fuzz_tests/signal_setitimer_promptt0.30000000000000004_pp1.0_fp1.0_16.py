import signal
# Test signal.setitimer()
#
# This test is only valid on systems that support the setitimer() system
# call.  It is not valid on Windows.
#
# This test is intended to be run under a debugger.  It will abort if
# the debugger does not respond to the SIGALRM signal.

import os
import sys
import signal
import time

# This test is only valid on systems that support the setitimer() system
# call.  It is not valid on Windows.
if not hasattr(signal, 'setitimer'):
    sys.exit(0)

def handler(signum, frame):
    print 'handler'
    sys.exit(0)

signal.signal(signal.SIGALRM, handler)

signal.setitimer(signal.ITIMER_REAL, 0.1, 0)

# The test will abort if the debugger does not respond to the SIGALRM
# signal.
while True:
    time.sleep(1)
