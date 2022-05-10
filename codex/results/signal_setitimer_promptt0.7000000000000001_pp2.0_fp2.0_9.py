import signal
# Test signal.setitimer() and signal.getitimer()
# On OSX, this is just a stub which throws an exception
#
# This is the only thing that signal.setitimer() and signal.getitimer()
# do that we test.  The rest of the constants are tested in test_signal.

import signal
import sys
import time

from test.support import run_unittest, import_module
if hasattr(signal, 'setitimer'):
    setitimer = signal.setitimer
else:
    import_module('signal')
    setitimer = signal.setitimer

if hasattr(signal, 'getitimer'):
    getitimer = signal.getitimer
else:
    import_module('signal')
    getitimer = signal.getitimer

class ItimerTest(unittest.TestCase):
    def test_itimer_basic(self):
        # Basic operation
        setitimer(signal.ITIMER_REAL, 1.0)
        time.sleep(1.1)
        self.assert
