import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtCore import QTimer
from PyQt4.QtTest import QTest


class TimeoutException(Exception):
    pass


def _timeout2(timeout, handler):
    # for python 2.x
    def handler2(signum, frame):
        raise TimeoutException()

    old_handler = signal.signal(signal.SIGALRM, handler2)
    signal.alarm(timeout)
    try:
        handler()
    finally:
        signal.signal(signal.SIGALRM, old_handler)
        signal.alarm(0)


def _timeout3(timeout, handler):
    # for python 3.x
    def handler2(signum, frame):
        raise TimeoutException()

    old_handler = signal.signal(signal.SIGALRM, handler2)
    signal.setitimer(signal.ITIMER_REAL, timeout)
