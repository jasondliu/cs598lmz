import signal
# Test signal.setitimer()
# Test siginterrupt() with SIGALRM and SA_RESTART

# Test siginterrupt with SIGALRM and SA_RESTART.
# Test 1: SIGINT not blocked, SA_RESTART not set
# Test 2: SIGINT not blocked, SA_RESTART set
# Test 3: SIGINT blocked, SA_RESTART not set
# Test 4: SIGINT blocked, SA_RESTART set

# the siginterrupt function alters the way the system handles
# the delivery of signals to the process.  A signal can be set
# to either be interrupted by the signal or to restart
# system calls interupted by the signal.

import os, sys, time
import unittest
from test.support import run_unittest, get_attribute, import_module

# utime is not available on all platforms
import errno
try:
    os.utime(__file__, None)
except OSError as e:
    if e.errno != errno.ENOSYS:
        raise
    utime = None
else:
    utime
