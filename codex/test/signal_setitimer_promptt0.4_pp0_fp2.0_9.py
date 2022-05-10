import signal
# Test signal.setitimer()
#
# This test is intended to test signal.setitimer() when the timer
# expires.  It is not intended to test the timer itself, which is
# tested by the test_signal_timer.py test.

import os
import signal
import sys
import time
import unittest
from test.support import run_unittest, captured_stdout

from test.support import reap_children, get_attribute

# Skip test if setitimer() is not available.
setitimer = get_attribute(signal, 'setitimer')
if setitimer is None:
    raise unittest.SkipTest("setitimer not available")

# Skip test if SIGALRM cannot be used.
alarm = get_attribute(signal, 'alarm')
if alarm is None:
    raise unittest.SkipTest("SIGALRM not available")

# Skip test if SIGALRM cannot be used.
alarm = get_attribute(signal, 'alarm')
