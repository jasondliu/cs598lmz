import signal
# Test signal.setitimer
class TestSetitimer(unittest.TestCase):
    def setUp(self):
        signal.signal(signal.SIGALRM, self.handler)

    def tearDown(self):
        pass

    def handler(self, sig, frame):
        self.signal = sig
        self.frame = frame

    def testit(self):
        signal.setitimer(signal.ITIMER_REAL, 1)
        time.sleep(1)
        self.assertEqual(self.signal, signal.SIGALRM)
        self.assertEqual(self.frame.f_code.co_name, 'sleep')
        self.assertEqual(self.frame.f_code.co_filename, __file__)

        signal.setitimer(signal.ITIMER_REAL, 0)
        self.assertRaises(ValueError, signal.setitimer, signal.ITIMER_REAL, -1)
        self.assertRaises(ValueError, signal.setitimer, signal.ITIMER_REAL,
