import signal
# Test signal.setitimer() and signal.getitimer()
import sys
import time
import unittest
if sys.platform == 'win32':
    setitimer = None
else:
    setitimer = signal.setitimer

class TestAlarm(unittest.TestCase):

    def setUp(self):
        self.oldalarm = signal.signal(signal.SIGALRM, lambda *args: None)

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.oldalarm)

    def test_alarm(self):
        signal.alarm(1)
        time.sleep(2)
        self.assertEqual(signal.alarm(0), 0)

    @unittest.skipUnless(hasattr(signal, 'setitimer'),
                         'test needs signal.setitimer()')
    def test_setitimer(self):
        self.assertRaises(TypeError, setitimer)
        self.assertRaises(ValueError, setitimer, signal.ITIMER_REAL,
