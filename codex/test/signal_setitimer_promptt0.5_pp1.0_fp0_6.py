import signal
# Test signal.setitimer() and signal.getitimer()

import os, time
from test.support import get_attribute, run_unittest

have_itimer = hasattr(signal, 'setitimer')

class ItimerTest(unittest.TestCase):
    # On OS X, the resolution of getitimer() is only 1/60s,
    # so we need to allow a larger error.
    epsilon = 0.01 if sys.platform == 'darwin' else 0.000001

    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)
        signal.setitimer(signal.ITIMER_REAL, 0, 0)

    def alarm_handler(self, *args):
        pass

