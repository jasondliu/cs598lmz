import signal
# Test signal.setitimer and signal.alarm.

import sys
import os
import time
from test.support import run_with_locale, requires_linux_version
from test.support.script_helper import assert_python_ok

# This test is Linux-specific because the signal.setitimer and
# signal.getitimer functions are not implemented on other platforms.
requires_linux_version(0, 2)

# The alarm() function is not available on Solaris.
if hasattr(signal, 'alarm'):
    alarm = signal.alarm
else:
    def alarm(n):
        pass

# Skip test if the getitimer() or setitimer() system calls are not available.
# This can happen on some Linux systems.
try:
    signal.setitimer(signal.ITIMER_REAL, 0)
except OSError as err:
    import errno
    if err.errno == errno.ENOSYS:
        raise unittest.SkipTest("getitimer() and/or setitimer() not available")
    raise

