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

