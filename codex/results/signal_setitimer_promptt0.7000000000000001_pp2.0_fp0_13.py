import signal
# Test signal.setitimer()

# Timer expiration handling not implemented on Windows
if sys.platform == 'win32':
    raise unittest.SkipTest("signal.setitimer() not implemented on Windows")

class TestSetitimer(unittest.TestCase):
    def setUp(self):
        self.sig_handler_called = 0

    def sig_handler(self, signum, frame):
        self.sig_handler_called += 1

    def test_setitimer(self):
        signal.signal(signal.SIGALRM, self.sig_handler)
        signal.setitimer(signal.ITIMER_REAL, 0.5, 0.5)
        time.sleep(4)
        self.assertTrue(self.sig_handler_called > 3 and self.sig_handler_called < 7)

    def test_setitimer_error(self):
        self.assertRaises(ValueError, signal.setitimer, -1, 0.5, 0.5)

if __name__ == '__main__':
   
