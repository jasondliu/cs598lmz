import signal
# Test signal.setitimer() and signal.getitimer()

# This test is linux-specific, because it depends on the
# precise behavior of the ITIMER_REAL timer.

import os
import sys
import time
import signal

# Skip test if getitimer/setitimer calls are not implemented
try:
    signal.setitimer(signal.ITIMER_REAL, 1, 0)
except AttributeError:
    raise unittest.SkipTest("getitimer/setitimer not implemented")

# Skip test if SIGALRM is not defined
try:
    signal.signal(signal.SIGALRM, lambda x,y: None)
except ValueError:
    raise unittest.SkipTest("SIGALRM not defined")

# Skip test if SIGALRM cannot be handled
try:
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
except ValueError:
    raise unittest.SkipTest("SIGALRM cannot be ignored")

# Skip test if SIGALRM cannot be blocked
try:
    signal.
