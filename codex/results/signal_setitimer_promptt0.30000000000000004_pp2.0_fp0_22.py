import signal
# Test signal.setitimer()
#
# This test is for the case where the signal handler is called
# from a different thread than the thread that set the timer.
#
# The test is a little tricky because the signal handler is
# called from the main thread, but the main thread is blocked
# waiting for the child thread to finish.  The child thread
# is blocked waiting for the main thread to finish.  To break
# the deadlock, the signal handler sets a global variable
# that the child thread is waiting on.

# Python imports
import os, sys, time
import unittest

# Local imports
from test import test_support

# Globals
handler_called = False

def handler(signum, frame):
    global handler_called
    handler_called = True
    # This is the tricky part.  We need to wake up the child
    # thread so it can finish.
    os.kill(os.getpid(), signal.SIGALRM)

def child():
    # Wait for the main thread to finish
    time.sleep(1)

class ItimerTest(unittest.TestCase):
