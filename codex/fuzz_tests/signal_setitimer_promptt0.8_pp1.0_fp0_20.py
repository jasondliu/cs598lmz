import signal
# Test signal.setitimer() behavior

import os
import sys
#from signal import signal as signal
import signal
import unittest
from test.script_helper import assert_python_ok

# Can't test on Windows, which doesn't implement setitimer() at all.
@unittest.skipIf(hasattr(signal, 'setitimer'),
                 'Windows does not support setitimer')
class SetitimerTest(unittest.TestCase):
    """Test the module functions."""

    def setUp(self):
        self.received = False
        self.old_handler = signal.signal(signal.SIGALRM, self.handler)
        self.addCleanup(signal.signal, signal.SIGALRM,
                        self.old_handler)

    def tearDown(self):
        signal.setitimer(signal.ITIMER_REAL, 0)
        if self.received:
            self.fail('received unexpected signal')

    def handler(self, signum, frame):
        self.received = True
        self.frame = frame
        self
