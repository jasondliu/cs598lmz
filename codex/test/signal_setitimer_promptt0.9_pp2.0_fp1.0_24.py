import signal
# Test signal.setitimer() with ITIMER_VIRTUAL 
# (Virtual-time timer is used to implement the x86 timers)
from test import test_support

class VirtualITimerTests(unittest.TestCase):
    def setUp(self):
        signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)

    def tearDown(self):
        signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)

    def test_itimer_virtual_value(self):
        # Raise an alarm after 0 s, then get the time remaining
        signal.setitimer(signal.ITIMER_VIRTUAL, 0, 0)
        self.assertTrue(signal.getitimer(signal.ITIMER_VIRTUAL)[0] < 0.1,
            "ITIMER_VIRTUAL conflicts with other tests, please retry")

