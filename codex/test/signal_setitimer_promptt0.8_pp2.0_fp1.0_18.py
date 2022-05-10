import signal
# Test signal.setitimer (siginterrupt() is deprecated on Python >= 2.6).
@unittest.skipUnless(hasattr(signal, 'setitimer'),
                     'need signal.setitimer()')
class SignalsTest(unittest.TestCase):
    def test_setitimer(self):
        def handler(signum, frame):
            raise KeyboardInterrupt
        old = signal.signal(signal.SIGALRM, handler)
        try:
            self.assertRaises(KeyboardInterrupt,
                              signal.setitimer, signal.ITIMER_REAL, 0.2)
        finally:
            signal.signal(signal.SIGALRM, old)

