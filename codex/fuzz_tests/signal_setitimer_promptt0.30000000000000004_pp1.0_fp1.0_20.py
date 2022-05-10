import signal
# Test signal.setitimer()
#
# This test is Linux specific.
#
# The test checks that the timer is not reset when it is already running.
#
# The test is based on the following code:
#
# import signal
# import time
#
# def handler(signum, frame):
#     print("handler")
#
# signal.signal(signal.SIGALRM, handler)
# signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# time.sleep(0.2)
# signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
# time.sleep(0.2)

# This test is Linux specific

import os
import sys
import time
import signal
import subprocess

from test.support import run_unittest, reap_children, get_attribute

# Skip test if setitimer() is not available
if not hasattr(signal, "setitimer"):
    raise unittest.SkipTest("setitimer() not available")

#
