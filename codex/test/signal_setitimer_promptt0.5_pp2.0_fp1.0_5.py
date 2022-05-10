import signal
# Test signal.setitimer() on the current platform.
#
# The test is skipped if the platform does not support setitimer().
#
# The test is skipped if the platform does not support SIGALRM.
#
# The test is skipped if the platform does not support SIGUSR1.

if not hasattr(signal, "setitimer"):
    raise unittest.SkipTest("setitimer() not available")

if not hasattr(signal, "SIGALRM"):
    raise unittest.SkipTest("SIGALRM not available")

if not hasattr(signal, "SIGUSR1"):
    raise unittest.SkipTest("SIGUSR1 not available")


class TestSetitimer(unittest.TestCase):
    def setUp(self):
        self.sigalrm_received = False
        self.sigusr1_received = False

    def sigalrm_handler(self, signum, frame):
        self.sigalrm_received = True

