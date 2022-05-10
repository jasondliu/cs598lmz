import signal
# Test signal.setitimer() and signal.getitimer() on non-POSIX systems.
import sys
from test import support


if sys.platform[:3] == 'win':
    SIGALRM = signal.SIGBREAK


class Alarm(Exception):
    pass


def alarm_handler(signal, frame):
    Alarm.was_caught = True
    raise Alarm


try:
    signal.signal(SIGALRM, alarm_handler)

    Alarm.was_caught = False
    signal.setitimer(signal.ITIMER_REAL, 0.1)
    support.run_with_locale('LC_ALL', 'C', support.check_syntax, '1+1')
    signal.setitimer(signal.ITIMER_REAL, 0)
    if not Alarm.was_caught:
        raise Exception("didn't catch alarm")
finally:
    signal.signal(SIGALRM, signal.SIG_DFL)
