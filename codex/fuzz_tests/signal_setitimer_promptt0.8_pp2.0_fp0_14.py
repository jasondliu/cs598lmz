import signal
# Test signal.setitimer() with an invalid value for which
import unittest

from test.support import run_unittest, requires_resource


@requires_resource('proc')
class ItimerExceptionTests(unittest.TestCase):

    def test_ITIMER_REAL(self):
        # This should not raise EINVAL.
        signal.setitimer(signal.ITIMER_REAL, 0, 1)

    def test_ITIMER_VIRTUAL(self):
        # If ITIMER_VIRTUAL is not implemented, a ValueError should be raised.
        # Otherwise, nothing should happen.
        try:
            signal.setitimer(signal.ITIMER_VIRTUAL, 0, 1)
        except ValueError:
            self.skipTest('ITIMER_VIRTUAL not available')

    def test_ITIMER_PROF(self):
        # If ITIMER_PROF is not implemented, a ValueError should be raised.
        # Otherwise, nothing should happen.
        try:
            signal.setitimer(signal.ITIM
