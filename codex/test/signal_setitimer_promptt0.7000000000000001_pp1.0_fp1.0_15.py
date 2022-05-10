import signal
# Test signal.setitimer()
import unittest
from test import support
signal.setitimer(signal.ITIMER_REAL, 2)
signal.setitimer(signal.ITIMER_REAL, 2, 1)
signal.setitimer(signal.ITIMER_VIRTUAL, 2)
signal.setitimer(signal.ITIMER_VIRTUAL, 2, 1)
signal.setitimer(signal.ITIMER_PROF, 2)
signal.setitimer(signal.ITIMER_PROF, 2, 1)


class AlarmException(Exception):
    pass


def alarm_handler(signum, frame):
    raise AlarmException
signal.signal(signal.SIGALRM, alarm_handler)


def itimer_retval(which, seconds, intervals):
    itimer_set = signal.setitimer(which, seconds)
    start_time = time.time()
    while time.time() - start_time < 2.0:
        pass
