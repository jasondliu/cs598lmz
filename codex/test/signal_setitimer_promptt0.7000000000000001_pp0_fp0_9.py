import signal
# Test signal.setitimer() on OS X.

import time, os
from test.support import requires, run_unittest, reap_children

requires('gui')

signals = []

if not hasattr(signal, 'setitimer'):
    try:
        import itimer
    except ImportError:
        raise unittest.SkipTest("itimer module not available")
    else:
        signal.setitimer = itimer.setitimer
        signal.getitimer = itimer.getitimer
        signal.ITIMER_REAL = itimer.ITIMER_REAL
        signal.ITIMER_VIRTUAL = itimer.ITIMER_VIRTUAL
        signal.ITIMER_PROF = itimer.ITIMER_PROF

class ItimerTest(unittest.TestCase):
    def setUp(self):
        self.original_handler = signal.signal(signal.SIGALRM, self.handler)
        signal.setitimer(signal.ITIMER_REAL, 0, 0)

