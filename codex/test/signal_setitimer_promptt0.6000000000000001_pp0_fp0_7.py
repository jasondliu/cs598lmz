import signal
# Test signal.setitimer()
#
# This test is Linux-specific, because it uses the ITIMER_REAL
# timer, which Linux is the only OS to support.

import os
import signal
import time
import sys

# The signal handler for the timer

