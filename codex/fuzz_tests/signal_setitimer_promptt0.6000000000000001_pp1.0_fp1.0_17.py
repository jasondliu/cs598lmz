import signal
# Test signal.setitimer, signal.getitimer, signal.alarm and signal.pause.
try:
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
except AttributeError:
    raise unittest.SkipTest("need signal.setitimer()")
import time
import os


class TestAlarms(unittest.TestCase):

    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)

    def alarm_handler(self, sig, frame):
        """SIGALRM handler"""
        self.alarm_fired = True

    def test_alarm(self):
        self.alarm_fired = False
        signal.alarm(1)
        time.sleep(2)
        self.assertTrue(self.alarm_fired)

    def test_alarm_zero(self):
        self.alarm_fired =
