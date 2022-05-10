import signal
# Test signal.setitimer()

import unittest
from test import support

class ItimerTest(unittest.TestCase):

    def setUp(self):
        self.signalled = False

    def handler(self, signum, frame):
        self.signalled = True

    def test_setitimer(self):
        signal.signal(signal.SIGALRM, self.handler)
        signal.setitimer(signal.ITIMER_REAL, 0.1)
        time.sleep(0.2)
        signal.setitimer(signal.ITIMER_REAL, 0)
        self.assertTrue(self.signalled)

def test_main():
    support.run_unittest(ItimerTest)

if __name__ == "__main__":
    test_main()
