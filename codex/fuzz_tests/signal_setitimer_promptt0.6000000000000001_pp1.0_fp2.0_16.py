import signal
# Test signal.setitimer with a single interval timer.

from test import support
import unittest
import time
import os

# Make sure we don't skip this test due to a missing signal
support.requires('signal')

# setitimer() is only available on systems that have getitimer()
has_itimer = hasattr(signal, "setitimer")

# getitimer() is only available on systems that have setitimer()
has_getitimer = hasattr(signal, "getitimer")


def alarm_received(n, stack):
    pass


class SetitimerTest(unittest.TestCase):

    @unittest.skipUnless(has_itimer, 'setitimer not available')
    def test_setitimer_basic(self):
        # The simplest test ...
        old_alarm_handler = signal.signal(signal.SIGALRM, alarm_received)
        self.addCleanup(signal.signal, signal.SIGALRM, old_alarm_handler)
        signal.setitimer(signal.ITIM
