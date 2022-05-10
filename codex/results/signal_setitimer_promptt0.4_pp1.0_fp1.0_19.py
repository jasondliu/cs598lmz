import signal
# Test signal.setitimer() and signal.getitimer()

# The test should be run in a subprocess, because it installs signal
# handlers that remain installed after the test finishes.

import os
import sys
import time
import unittest
from test import support

# The following constants are defined in <sys/time.h> on Linux.
ITIMER_REAL = 0
ITIMER_VIRTUAL = 1
ITIMER_PROF = 2

# This is the number of seconds between the epoch and the first time
# setitimer() is called in the test.
EPOCH = 1546300800.0

# This is the number of seconds between the epoch and the second time
# setitimer() is called in the test.
EPOCH_PLUS_ONE = EPOCH + 1.0

# This is the number of seconds between the epoch and the third time
# setitimer() is called in the test.
EPOCH_PLUS_TWO = EPOCH + 2.0

# This is the number of seconds between the epoch and the fourth time
# setitimer() is
