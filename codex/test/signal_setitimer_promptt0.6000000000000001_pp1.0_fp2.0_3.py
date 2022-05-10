import signal
# Test signal.setitimer() with alarm()

# check if alarm() is supported
try:
    signal.alarm(1)
    signal.alarm(0)
except AttributeError:
    raise unittest.SkipTest('alarm() not supported')

import time, os, sys

class AlarmTest(unittest.TestCase):
    def handler(self, signum, frame):
        self.signum = signum
        self.frame = frame
        self.alarm_caught = 1
        self.alarm_received = time.time()
        self.alarm_delta = self.alarm_received - self.alarm_sent

    def setUp(self):
        self.alarm_sent = time.time()
        self.alarm_caught = 0
        self.old_alarm = signal.signal(signal.SIGALRM, self.handler)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_alarm)

