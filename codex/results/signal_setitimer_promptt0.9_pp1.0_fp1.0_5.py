import signal
# Test signal.setitimer
from test import support
import time
from test.support import TESTFN, unlink
from Lib.multiprocessing import Process, freeze_support
from Lib._testcapi import get_errno, set_errno
from Lib import subprocess
from Lib import _testcapimodule
import os

FAILED = ()

class AlarmException(Exception):
    pass

def alarm_handler(signum, frame):
    raise AlarmException

def testfn():
    # Wait until SIGALRM arrives, test if it's possible to handle it
    # using SIG_IGN or a handler.
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    time.sleep(1)
    signal.signal(signal.SIGALRM, alarm_handler)
    time.sleep(1)
    signal.signal(signal.SIGALRM, alarm_handler)
    time.sleep(6)

def alarm_child():
    # The parent will set an alarm of 2 seconds, we need to be sure that
    # time
