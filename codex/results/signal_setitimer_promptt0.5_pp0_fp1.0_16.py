import signal
# Test signal.setitimer()
# 
# This is a test of signal.setitimer().  It is intended to be run in a
# subprocess by test_signal.  It is not run directly because
# setitimer() doesn't work on the main thread.
# 
# The test runs for 5 seconds.  During this time, it sets a signal
# handler for SIGALRM and calls signal.setitimer() every second for 5
# seconds.  It checks that the signal handler is called at least once
# during each second.
# 
# The test is run under the following conditions:
# 
# - With and without a timeout value.
# - With and without the SA_RESTART flag.
# - With and without the signal handler installed before the call to
#   setitimer().
# 
# The test is repeated for each of ITIMER_REAL, ITIMER_VIRTUAL and
# ITIMER_PROF.

import signal
import sys
import time
import os
import unittest
from test import support

# The test runs for 5 seconds.
TEST_DUR
