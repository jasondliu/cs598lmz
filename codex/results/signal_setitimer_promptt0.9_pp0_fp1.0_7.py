import signal
# Test signal.setitimer() with signal.ITIMER_REAL

from test.support import verbose, import_module, get_attribute
import_module('signal')


def handler(signum, frame):
    """Handler raises the SystemExit exception."""
    print('handler')
    raise SystemExit


def alarmhandler(signum, frame):
    """Handler raises the Alarm exception."""
    print('alarmhandler')
    raise Alarm


class Alarm(Exception):
    """This is an exception that can be raised in the handler."""
    pass


print('Test Setting SIGALRM and verifying timer is started')
# Set a signal handler for alarm
signal.signal(signal.SIGALRM, alarmhandler)
signal.setitimer(signal.ITIMER_REAL, 0.5)
if verbose:
    print('stop')
try:
    import time
    time.sleep(1)
except Alarm:
    if verbose:
        print('go')
else:
    print('setitimer did not work')
    signal.setitimer
