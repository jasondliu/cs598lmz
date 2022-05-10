import signal
# Test signal.setitimer
# This is Linux specific, but that's all we support anyway

import sys

if sys.platform != 'linux':
    raise ImportError("test only works on linux")

import os
import time

from test.support import run_unittest, requires_linux_version, requires_linux_version_or_higher
requires_linux_version(2, 6, 0)

from test.support import cpython_only
cpython_only("test only works on CPython")

try:
    from test.support import find_unused_port
except ImportError:
    from test.script_helper import find_unused_port

from test.fork_wait import fork_wait

#
# Test setitimer()
#

def alarm_received(n, stack):
    print('Alarm received')

def setitimer_signal_alarm():
    signal.signal(signal.SIGALRM, alarm_received)
    # Linux's setitimer() will reset the handler to SIG_DFL, so we have to
    # re-set it on
