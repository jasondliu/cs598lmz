import signal
# Test signal.setitimer/signal.setitimer

class SetitimerTestCase(unittest.TestCase):

    def test_setitimer(self):
        signalled = []

        def handler(signum, frame):
            signalled.append(signum)
            raise RuntimeError("should not get here")

        signal.signal(signal.SIGALRM, handler)
        signal.setitimer(signal.ITIMER_REAL, 0, 0.1)
        signal.alarm(0)
        # And we should not have been interrupted
        self.assertEqual(signalled, [])

        signal.signal(signal.SIGALRM, handler)
        signal.setitimer(signal.ITIMER_REAL, 0, 0.1)
        time.sleep(0.4)
        self.assertGreaterEqual(signalled.count(signal.SIGALRM), 1)
        self.assertLess(signalled.count(signal.SIGALRM), 5)
