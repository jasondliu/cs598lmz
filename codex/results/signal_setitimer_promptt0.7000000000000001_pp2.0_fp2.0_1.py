import signal
# Test signal.setitimer
# It's not available on Windows.
try:
    signal.setitimer
except AttributeError:
    raise ImportError("skipped because signal.setitimer is not defined")

from signal import SIGALRM, ITIMER_REAL, ITIMER_VIRTUAL, ITIMER_PROF
import errno
from test import support
import unittest

# Test the accuracy of signal.setitimer().
# This test requires a fast CPU and will probably fail on slow machines.

# The interval used for the tests is 0.1 seconds.  On some machines,
# this is too short for setitimer() to work properly.  (On Windows,
# for example, the smallest allowed interval is 0.5 seconds.)  If this
# is a problem, you can change the interval to a larger value.
# However, if you set it too large, the test will take too long to
# run and may fail on slow machines.
INTERVAL = 0.1

# The number of intervals to use in each test.  The total test time
# will be INTERVAL * NUM_INTERVALS seconds
