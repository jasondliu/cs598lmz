import signal
# Test signal.setitimer()
#
# This test will pass if setitimer() works as expected
#
# This test is intended to be run from the Python test suite.

import unittest

class ItimerTest(unittest.TestCase):
    def setUp(self):
        self.called = 0
        signal.signal(signal.SIGALRM, self.handler)

    def tearDown(self):
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

    def handler(self, signum, frame):
        self.called += 1

    def test_itimer_zero(self):
        # Test zero time
        signal.setitimer(signal.ITIMER_REAL, 0)
        self.assertEqual(self.called, 1)

    def test_itimer_non_zero(self):
        # Test non-zero time
        signal.setitimer(signal.ITIMER_REAL, 0.2)
       
