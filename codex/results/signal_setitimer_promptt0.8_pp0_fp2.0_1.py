import signal
# Test signal.setitimer
import sys
import time

import unittest
from test import support


class ItimerTest(unittest.TestCase):

    def setUp(self):
        # a function to raise the alarm signal
        self.raised = False
        def set_raised(*args):
            self.raised = True
        self.old_alarm = signal.signal(signal.SIGALRM, set_raised)

        if sys.platform[:3] in ('win', 'os2', 'riscos') or \
           sys.platform == 'atheos':
            raise unittest.SkipTest('can not test on %r' % sys.platform)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)

    def testConstants(self):
        self.assertEqual(signal.ITIMER_REAL, 0)
        self.assertEqual(signal.ITIMER_VIRTUAL, 1)
        self.assertEqual(signal.ITIMER_PROF, 2)


