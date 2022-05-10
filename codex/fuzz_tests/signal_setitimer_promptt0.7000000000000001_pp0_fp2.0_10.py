import signal
# Test signal.setitimer
#
# The function must be called as root, otherwise ValueError is raised.

import sys
import unittest
from test import support

signal = support.import_module('signal')

class TestSetitimer(unittest.TestCase):

    def test_itimer_types(self):
        # Only ITIMER_REAL is supported.
        self.assertRaises(ValueError, signal.setitimer,
                          'unknown', 0)

    @unittest.skipUnless(hasattr(signal, 'alarm'),
                         'signal.alarm() required')
    def test_alarm(self):
        # Using signal.alarm, we reset the interval to zero seconds.
        # This will cause any pending alarm to be triggered immediately.
        # We then restore the old interval.

        # The following code uses time.sleep, which is known to be
        # unreliable on some platforms.  If the test fails, please don't
        # be tempted to fix it by changing the 0.1 to a larger value!
        # The right fix is to make time.
