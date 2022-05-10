import signal
# Test signal.setitimer
# Signal handling is not straightforward.  On some platforms, the handler
# is run on a separate thread.  On others (e.g. Solaris), the handler is run
# on the same thread.
# Here's how to set up a signal handler to run on a separate thread,
# if possible.

# This is a test for Issue #17096.  This test may need to be disabled
# on some platforms.
class TestSignalSetitimer(unittest.TestCase):
    def test_setitimer(self):
        # 1. Establish a signal handler, in a way that doesn't interfere
        # with the handling of signals by the signal module.
        class Timeout(Exception):
            def __init__(self, signum, itimer):
                msg = "got signal {!r}, itimer {:.2f}, {:.2f}".format(
                    signum, itimer[0], itimer[1])
                super(Timeout, self).__init__(msg)

        def handler(signum, frame):
            itimer = signal.setitimer(signal
