import signal
# Test signal.setitimer

import unittest
from test import support

signal_names = [
    "SIGALRM", "SIGVTALRM", "SIGPROF",
]

class TestSetitimer(unittest.TestCase):

    def test_setitimer(self):
        # Test that signal.setitimer raises a ValueError if the interval
        # is negative.
        for name in signal_names:
            signal_name = getattr(signal, name, None)
            if signal_name is None:
                continue
            try:
                signal.setitimer(signal_name, -1, 0)
            except ValueError:
                pass
            else:
                self.fail("setitimer did not raise ValueError")

