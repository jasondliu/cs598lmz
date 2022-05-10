import signal
# Test signal.setitimer()

# This test requires some manual checking of the output
# to ensure that the test is behaving as expected.

# Try:
# $ ./python -m test test_idle
# or preferably
# $ ./python Tools/scripts/run_tests.py /path/to/test_idle.py

import gc
import os
import test.support
import time
import unittest
from test.support import verbose

# Try to get an IDLE window.
# If this fails, the test will still run,
# but with less user-friendly output.
try:
    import idlelib.idle
    idle_installed = True
except ImportError:
    idle_installed = False

# On win32 signal module does not exist
if hasattr(signal, 'setitimer'):
    setitimer = signal.setitimer
else:
    def setitimer(*args):
        pass


@unittest.skipUnless(idle_installed, 'idle not installed')
@unittest.skipUnless(hasattr(signal, 'setitimer'), '
