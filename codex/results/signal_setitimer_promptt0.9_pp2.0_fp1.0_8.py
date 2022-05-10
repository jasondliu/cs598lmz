import signal
# Test signal.setitimer and signal.getitimer
#
# This requires the use of alarm(), which is only available on some systems,
# and isn't available on Windows.
#
# Requires the use of subprocess, which isn't available on AppEngine

import os, sys, errno, time, subprocess
from test.test_support import run_unittest, import_module

if hasattr(signal, 'setitimer') and hasattr(signal, 'getitimer'):
    # For architectures where all the relevant system calls are
    # implemented, it's good to run a test on the system calls 
    # themselves.
    import _testcapi
    class ItimerSysCallsTest(unittest.TestCase):
        def _checkitimer(self, name, mode, expected):
            # Try to determine the expected value.  On some systems
            # (e.g. FreeBSD), alarm always rounds up to the next second,
            # and on other systems (e.g. Linux) it depends on the resolution
            # of the hardware clock.
            now = time.time()
            secs
