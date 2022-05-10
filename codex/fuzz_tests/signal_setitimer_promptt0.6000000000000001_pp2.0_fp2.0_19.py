import signal
# Test signal.setitimer with SIGPROF.

import unittest
import os
import test.support

from test.support import os_helper

if os_helper.signal_name('SIGPROF') is None:
    raise unittest.SkipTest("SIGPROF not supported")

pid = os.getpid()

def handler(*args):
    print("handler", args)
    raise SystemExit

class TestSetitimer(unittest.TestCase):
    def setUp(self):
        self.saved_handler = signal.signal(signal.SIGPROF, handler)

    def tearDown(self):
        signal.signal(signal.SIGPROF, self.saved_handler)

    def test_setitimer(self):
        if os.fork() == 0:
            signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
            for i in range(5):
                os.kill(pid, signal.SIGPROF)
        else:
            os.wait()

