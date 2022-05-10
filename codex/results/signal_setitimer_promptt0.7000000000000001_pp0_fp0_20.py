import signal
# Test signal.setitimer
# Valgrind will complain about setitimer and sigaction, but
# that's in the C library and not our code.
signal.setitimer(signal.ITIMER_REAL, 1.0, 3.0)

# Test signal.set_wakeup_fd
# Set the wakeup fd to be non-blocking
fd = os.open("/dev/null", os.O_RDONLY | os.O_NONBLOCK)
signal.set_wakeup_fd(fd)
os.close(fd)

# Test the faulthandler module
import faulthandler
faulthandler.enable()

# Check that the fork() warning is displayed (and only once)
class ForkTests(unittest.TestCase):
    def setUp(self):
        self.log = support.captured_stderr
        del self.log[:]
        self.warn = ('\n'
            '===========================\n'
            'WARNING: fork() called in test.\n'
            '===========================\n
