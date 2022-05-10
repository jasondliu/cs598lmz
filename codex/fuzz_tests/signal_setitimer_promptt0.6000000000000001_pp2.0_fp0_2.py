import signal
# Test signal.setitimer and signal.alarm

import os
import sys
from test import support
import signal
import subprocess
import time
import unittest

from test.support import reap_children, get_attribute
from test.support.script_helper import assert_python_ok

class AlarmException(Exception):
    pass

def alarm_received(n, frame):
    raise AlarmException

class ItimerTest(unittest.TestCase):
    # On some systems (e.g. FreeBSD and OpenBSD), the kernel limits the
    # amount of time that the process can be sleeping for.  If the
    # process calls sleep() for a longer time than the system allows,
    # the process will sleep until the next clock tick, and then
    # return early with a short sleep time.
    #
    # This means that some of the tests in this file will fail if the
    # requested sleep time is longer than the system allows.  The
    # value of ITIMER_REAL_MAX is the highest sleep time that we know
    # we can use on all systems.  On most systems, it
