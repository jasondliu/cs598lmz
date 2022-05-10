import signal
# Test signal.setitimer and signal.alarm

import unittest
from test import support

import os
import time
import threading
import signal

from test.support import reap_children


class TestSetitimer(unittest.TestCase):

    def test_setitimer_basic(self):
        # test basic setitimer-based timing
        # POSIX specifies that the resolution of timer services is at least
        # 20 milliseconds, so our tests will use times greater than this.
        TIME = 0.25
        ACCEPTABLE_ERROR = 0.05

        # a lock used for communicating time values between the main thread
        # and the signal handler.
        ready = threading.Lock()
        ready.acquire()

        def handler(signum, frame):
            # just record the current time
            handler.when = time.time()
            ready.release()

        handler.when = None

        # register the handler for SIGALRM
        old_handler = signal.signal(signal.SIGALRM, handler)

