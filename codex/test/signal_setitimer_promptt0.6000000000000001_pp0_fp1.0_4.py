import signal
# Test signal.setitimer
class test_setitimer(unittest.TestCase):
    def test_setitimer(self):
        self.assertRaises(ValueError, signal.setitimer,
                          signal.ITIMER_REAL, -1, 0)
        self.assertRaises(ValueError, signal.setitimer,
                          signal.ITIMER_REAL, -1, 1)
        self.assertRaises(ValueError, signal.setitimer,
                          signal.ITIMER_REAL, 1, -1)
        self.assertRaises(ValueError, signal.setitimer,
                          signal.ITIMER_VIRTUAL, -1, 0)
        self.assertRaises(ValueError, signal.setitimer,
                          signal.ITIMER_VIRTUAL, -1, 1)
        self.assertRaises(ValueError, signal.setitimer,
                          signal.ITIMER_VIRTUAL, 1, -1)
