import signal
# Test signal.setitimer()
#
# This test checks that the following system calls return the expected
# error:
#  - setitimer()
# Note:
#  - EINVAL
#
# The following tests are not tested:
#  - ITIMER_VIRTUAL
#    The kernel does not support this timer.
#  - ITIMER_PROF
#    The kernel does not support this timer.

import os
import sys
import time
import unittest
from test.support import run_unittest, get_attribute


class SiginterruptTest(unittest.TestCase):

    def test_setitimer(self):
        ITIMER_REAL = 0
        ITIMER_VIRTUAL = 1
        ITIMER_PROF = 2
        # setitimer() returns the old value
        oldvalue = signal.setitimer(ITIMER_REAL, 0, 0)
        self.assertTrue(isinstance(oldvalue, tuple))
        self.assertEqual(len(oldvalue), 3)
