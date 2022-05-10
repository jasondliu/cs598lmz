import signal
# Test signal.setitimer() which is the same as the BSD setitimer() syscall.

import time
import unittest

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

class TestSignal(unittest.TestCase):

    def setUp(self):
        signal.signal(signal.SIGALRM, alarm_handler)

    def tearDown(self):
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, signal.SIG_DFL)

    def catch_alarm(self, delay):
        signal.setitimer(signal.ITIMER_REAL, delay)
        try:
            time.sleep(delay*2)
        except Alarm:
            pass
        else:
            self.fail("didn't catch alarm")

    def test_itimer_zero(self):
        self.catch_alarm(0)
        time.sleep(0.1)

