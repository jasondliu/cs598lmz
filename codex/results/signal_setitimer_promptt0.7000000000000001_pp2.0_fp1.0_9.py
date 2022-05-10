import signal
# Test signal.setitimer() and signal.getitimer()
# Note:
#   - timer resolution is hardware dependent;
#   - often limited to 10-20 ms.

import sys
import time

from test import support
from test.support import bigmemtest, precisionbigmemtest

try:
    signal.setitimer(signal.ITIMER_REAL, 1, 1)
except (OSError, AttributeError):
    raise unittest.SkipTest("need setitimer()")

def alarm_received(n, stack):
    "Callback: signal handler"
    sys.stderr.write('Alarm %d received\n' % n)
    time.sleep(2)

def test_main():
    if sys.platform == 'win32':
        # How can we test on Windows?
        raise unittest.SkipTest("can't test on Windows")
    # Register a signal handler
    signal.signal(signal.SIGALRM, alarm_received)
    # Schedule the first alarm in 2 seconds
    signal.setitimer(signal.ITIMER_
