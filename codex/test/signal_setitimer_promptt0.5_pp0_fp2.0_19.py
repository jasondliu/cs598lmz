import signal
# Test signal.setitimer, signal.getitimer, signal.ITIMER_REAL and
# signal.ITIMER_VIRTUAL.

# This test is based on the itimer.c test from the GNU C library.

import sys
import time
import unittest
from test import support

def handler(signum, frame):
    pass

