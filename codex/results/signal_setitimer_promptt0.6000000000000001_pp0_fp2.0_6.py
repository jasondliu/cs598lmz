import signal
# Test signal.setitimer
# This is a test for a bug we had in Python 2.6.
# The bug was that the signal handler for SIGCHLD would
# sometimes be called twice, and the second time it was called
# with a zombie process (a child that had already exited).
# The problem was that we were not setting the ITIMER_REAL
# timer to 0 before calling waitpid().
#
# It's hard to be sure this test is really testing the bug,
# but we haven't seen the bug in a while, so here's hoping.

import os, time, array
import unittest
from test.test_support import run_unittest

class SigchldWaiter(object):
    def __init__(self):
        self.pid = None
        self.signalled = False

    def handler(self, signum, frame):
        self.signalled = True
        os.waitpid(self.pid, 0)

    def wait(self):
        self.pid = os.fork()
        if self.pid == 0:
            # child
            time.sleep(1)
           
