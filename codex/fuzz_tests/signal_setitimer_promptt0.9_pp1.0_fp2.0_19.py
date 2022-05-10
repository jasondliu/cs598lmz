import signal
# Test signal.setitimer

import unittest
from test.support import run_unittest, cpython_only

@cpython_only
class TestItimer(unittest.TestCase):
    def gettimeofday(self):
        import time
        return time.time()

    def setitimer(self, which, seconds, inittime=None):
        import signal
        seconds, inittime = self.itimer_params(which, seconds, inittime)
        if inittime == 0:
            sig = 0
        else:
            sig = signal.SIGALRM
        return signal.setitimer(which, seconds, inittime), sig

    def itimer_params(self, which, seconds, inittime):
        if inittime is None:
            inittime = seconds
        self.assertTrue(which in (signal.ITIMER_REAL, signal.ITIMER_VIRTUAL,
                                  signal.ITIMER_PROF))
        self.assertTrue(type(seconds) in (int, float))
        self.assertTrue(type
