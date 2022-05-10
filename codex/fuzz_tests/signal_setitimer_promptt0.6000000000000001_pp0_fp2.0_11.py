import signal
# Test signal.setitimer()
#

import unittest

from test import support

class ItimerTestCase(unittest.TestCase):

    def setUp(self):
        self.called = 0

    def handler(self, *args):
        self.called += 1

    def test_signal(self):
        # The following code can hang forever if the bug is present
        # This requires the timer to fire more than once
        signal.signal(signal.SIGALRM, self.handler)
        signal.setitimer(signal.ITIMER_REAL, .01, .02)
        # Busy wait for the signal to be delivered
        while self.called < 2:
            pass

    def test_siginterrupt(self):
        # Test that signal.siginterrupt() works
        signal.signal(signal.SIGALRM, self.handler)
        signal.setitimer(signal.ITIMER_REAL, .01, 0)
        # Busy wait for the signal to be delivered
        while self.called == 0:
            pass
