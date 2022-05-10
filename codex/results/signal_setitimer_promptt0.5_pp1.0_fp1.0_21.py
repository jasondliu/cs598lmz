import signal
# Test signal.setitimer()

import unittest
from test.support import run_unittest, reap_children, get_attribute

from test.script_helper import assert_python_ok, assert_python_failure

class SignalTests(unittest.TestCase):

    def setUp(self):
        # Some tests mess with the alarm, which is shared between
        # threads, so we need to reset it here to make sure that it
        # doesn't mess with other tests.
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        signal.setitimer(signal.ITIMER_REAL, 0, 0)

    def tearDown(self):
        # Make sure we don't leave an alarm running that could mess
        # with other tests.
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        signal.setitimer(signal.ITIMER_REAL, 0, 0)

    def test_itimer_zero(self):
        # bug 1042928: Check that setting an itimer to
