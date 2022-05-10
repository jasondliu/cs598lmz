import signal
# Test signal.setitimer. Broken on some platforms.
try:
    signal.setitimer(signal.ITIMER_REAL, 0.1)
    HAVE_SETITIMER = True
except ValueError:
    HAVE_SETITIMER = False

from test import support
threading = support.import_module('threading')

# Some timing problems are inherent in these tests.
# Timeouts should never be less than 0.2, and preferably more.
# Timeouts in the 0.2-1.0 range are especially sensitive to timing
# variation, and probably shouldn't be used at all.

TIMEOUT1 = 1.0
TIMEOUT2 = 5.0

def handler(signum, frame):
    print("handler", signum, frame)

def handler1(signum, frame):
    raise SystemExit

def handler2(signum, frame):
    import signal
    signal.alarm(4)

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

def sleeper(delay):
    time.sleep(delay
