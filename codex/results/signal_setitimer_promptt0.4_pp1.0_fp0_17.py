import signal
# Test signal.setitimer() and signal.getitimer()

import sys
import time

from test import support

signal_module = support.import_module('signal')

def setitimer_alarm(n):
    # Call signal.setitimer() from a signal handler for SIGALRM,
    # to check that it can be called from a signal handler.
    signal_module.setitimer(signal_module.ITIMER_REAL, 0.2)

def alarm_received(n, stack):
    pass

def test_setitimer():
    # Test use of signal.setitimer() to create a busy loop.
    # Without the signal handler, the busy loop consumes 100% CPU.
    # With the signal handler, the busy loop consumes almost no CPU.
    # The handler is called often enough to keep the busy loop from
    # consuming much CPU.
    signal_module.signal(signal_module.SIGALRM, setitimer_alarm)
    signal_module.setitimer(signal_module.ITIMER_REAL, 0.2,
