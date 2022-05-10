import signal
# Test signal.setitimer() and signal.getitimer()

# The signal module is not available on Windows.
import sys
if sys.platform == "win32":
    raise ImportError("signal not supported")

import unittest
from test import support

# Skip this test if the platform doesn't have setitimer() or
# getitimer().
getitimer = getattr(signal, "getitimer", None)
setitimer = getattr(signal, "setitimer", None)
if getitimer is None or setitimer is None:
    raise unittest.SkipTest("platform doesn't support getitimer() or "
                            "setitimer()")


def alarm_received(n, stack):
    raise AssertionError("SIGALRM not received")

class ItimerTest(unittest.TestCase):

    def setUp(self):
        self.sigalrm_handler = signal.signal(signal.SIGALRM, alarm_received)

