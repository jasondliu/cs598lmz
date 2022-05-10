import signal
# Test signal.setitimer() and signal.getitimer()

import os
import time
import unittest

from test.support import run_unittest
from test.support import import_module

# Skip the test if itimer support is not available
signal = import_module('signal')
if not hasattr(signal, 'setitimer'):
    raise unittest.SkipTest("itimer support needed for this test.")

if hasattr(signal, 'alarm'):
    # Some systems (e.g. Linux) provide alarm() as a system call, but
    # not the POSIX timers.
    raise unittest.SkipTest("POSIX timers not available on this system.")

# This test is not guaranteed to work on all systems.  The values
# returned by getitimer() may be slightly different than those set by
# setitimer().  The test passes if the difference is no greater than
# .1 seconds.  This value is determined by trial-and-error on a
# variety of systems.

EPSILON = .1

