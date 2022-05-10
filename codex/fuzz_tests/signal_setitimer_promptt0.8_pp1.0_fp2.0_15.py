import signal
# Test signal.setitimer() with various flags

import unittest
from test import support

class ItimerTest(unittest.TestCase):
    def setUp(self):
        self.called = 0

    def handler(self, signum, frame):
        self.called += 1

    def test_itimer(self):
        # Test with 0 delay as we don't want to wait for the timer to expire.
        delay = 0
        for which in ('PROF', 'REAL', 'VIRTUAL'):
            self.called = 0
            self.assertRaises(ValueError, signal.setitimer, which, delay)
            self.assertEqual(self.called, 0)

    def test_itimer_prof(self):
        delay = 0.1 # short delay after which the timer will expire
        which = 'PROF'
        # Test that SIGPROF is generated (it should with itimer_prof.c)
        signal.signal(signal.SIGPROF, self.handler)
        self.called = 0
        signal.setitimer(which, delay)
       
