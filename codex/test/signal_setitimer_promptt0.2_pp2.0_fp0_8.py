import signal
# Test signal.setitimer()
#
# This test is Linux specific.
#
# The test is based on the following code:
#
# import signal
# import time
#
# def handler(signum, frame):
#     print "handler"
#
# signal.signal(signal.SIGALRM, handler)
# signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
#
# while True:
#     time.sleep(1)
#
# The test is expected to print "handler" every 0.1 seconds.
#
# The test is expected to pass.

import os
import time
import unittest


class SetitimerTest(unittest.TestCase):

    def test_setitimer(self):
        pid = os.fork()
        if pid == 0:
            # Child process
            signal.signal(signal.SIGALRM, signal.SIG_DFL)
            signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
            time.sleep
