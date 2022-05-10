import signal
# Test signal.setitimer
import signal, os, unittest

class TestItimer(unittest.TestCase):

    def handler_itimer(self, signum, frame):
        self.handler_itimer_calls += 1
        raise SystemExit

    def handler_signal(self, signum, frame):
        self.handler_signal_calls += 1
        raise SystemExit

    def setUp(self):
        self.handler_itimer_calls = 0
        self.handler_signal_calls = 0

    def tearDown(self):
        if hasattr(signal, "setitimer"):
            signal.setitimer(signal.ITIMER_REAL, 0)
        # Make sure we set SIGINT back to the default handler
        signal.signal(signal.SIGINT, signal.SIG_DFL)

    def test_itimer_types(self):
        if hasattr(signal, "setitimer"):
            for t in (signal.ITIMER_REAL, signal.ITIMER_VIRTUAL,

