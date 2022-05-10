import signal
# Test signal.setitimer and signal.getitimer

from test.support import requires_type_collecting
import unittest
from test.support.script_helper import assert_python_ok
import signal as py_signal
import os

@unittest.skipUnless(hasattr(signal, "setitimer"),
                     "test needs signal.setitimer()")
class ItimerTests(unittest.TestCase):
    def setUp(self):
        signal.signal(signal.SIGALRM, self.handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

    def handler(self, signo, frame):
        self.seen_signal = True

    def test_getitimer(self):
        timer = signal.getitimer(signal.ITIMER_REAL)
        # This assert won't catch all errors,
        # but it'll catch some.
        self.assertEqual(len(timer), 2)

