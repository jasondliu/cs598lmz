import signal
# Test signal.setitimer() and signal.alarm()
from test import support
import time
from time import sleep
try:
    import threading
except ImportError:
    threading = None


VERBOSE = support.verbose

def handler1(*args):
    if VERBOSE:
        print("handler1:", args)
    raise SystemExit

def handler2(*args):
    if VERBOSE:
        print("handler2:", args)
    raise SystemExit

class AlarmTest(unittest.TestCase):

    def setUp(self):
        signal.signal(signal.SIGALRM, signal.SIG_IGN)

    def tearDown(self):
        signal.alarm(0)

    def getitimer(self):
        # Return the tuple (delay, remaining)
        delay, remaining = signal.getitimer(signal.ITIMER_REAL)
        return (delay, time.time() + remaining)

    def setitimer(self, which, seconds, interval=0):
        delay, remaining = self.getitimer()
       
