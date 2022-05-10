import signal
# Test signal.setitimer, which is not supported on windows
try:
    signal.setitimer
except AttributeError:
    raise nose.SkipTest('signal.setitimer not supported')

from numba import jit
from numba import unittest_support as unittest

def sig_handler(signum, frame):
    raise AssertionError("received signal %d, exiting from %s"
                         % (signum,
                            "setitimer" if signum == signal.SIGALRM else
                            "sigaction"))

def setitimer_alarm_signal_handler():
    signal.signal(signal.SIGALRM, sig_handler)

def setitimer_fnc(sec, usec):
    setitimer_alarm_signal_handler()
    signal.setitimer(signal.ITIMER_REAL, sec, usec)
    import time
    time.sleep(0.1)

def sigaction_fnc(sec):
    signal.signal(signal.SIGALRM, sig_handler)
