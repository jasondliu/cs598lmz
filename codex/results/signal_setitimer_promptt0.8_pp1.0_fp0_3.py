import signal
# Test signal.setitimer(), unix only
class TimerTest(unittest.TestCase):

    def handler(self, sig, frame):
        self.called = True

    def setUp(self):
        self.called = False
        signal.signal(signal.SIGALRM, self.handler)

    @unittest.skipUnless(hasattr(signal, 'setitimer'),
                         'requires signal.setitimer()')
    def testITimerAccuracy(self):
        # Issue #15724: Check that the timer fires for small intervals.
        for i in range(100):
            signal.setitimer(signal.ITIMER_REAL, 0.000001, 0)
            t = time.time()
            while not self.called and time.time() <= t + 0.01:
                pass
            self.assertTrue(self.called,
                            "signal.setitimer() did not fire after 0.000001 seconds")
            self.called = False

    @unittest.skipUnless(hasattr(signal, 'setitimer'),
                         '
