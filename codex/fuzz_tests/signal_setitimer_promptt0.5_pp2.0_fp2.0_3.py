import signal
# Test signal.setitimer

from test import support
from test.support import import_module

signal = import_module('signal')

def handler(signum, frame):
    pass

signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

# Make sure SIGALRM is not delivered yet.
signal.pause()

signal.setitimer(signal.ITIMER_REAL, 0, 0)
