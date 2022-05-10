import signal
# Test signal.setitimer() and signal.getitimer()

import os
import sys
import time
import unittest
from test import support

try:
    signal.setitimer
except AttributeError:
    raise unittest.SkipTest("requires setitimer()")

if sys.platform == 'win32':
    raise unittest.SkipTest("cannot test setitimer() reliably on windows")

#
# Test whether the expected signals are delivered.
#

def handler1(*args):
    "Generic signal handler."
    pass

def handler2(*args):
    "Generic signal handler."
    pass

def handler3(*args):
    "Generic signal handler."
    pass

signum = support.find_unused_gdb_port()

def alarm_received():
    "Return whether the alarm signal was received."
    try:
        os.kill(os.getpid(), 0)
    except OSError as e:
        return e.errno == support.EPERM
    else:
        return False

