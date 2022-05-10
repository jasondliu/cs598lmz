import signal
# Test signal.setitimer() and signal.getitimer()

# setitimer() isn't supported on Windows, so skip this test there
if sys.platform.startswith("win"):
    raise unittest.SkipTest("Windows doesn't support setitimer()")

# Irix raises an EINVAL for ITIMER_PROF, so skip that too
if sys.platform.startswith("irix"):
    raise unittest.SkipTest("Irix doesn't support ITIMER_PROF")

import time, errno

sec = 1.0

def handler(signum, frame):
    pass

class TimeIt(unittest.TestCase):
    def setUp(self):
        self.old_handler = signal.signal(signal.SIGALRM, handler)
        self.set_time = sec
        self.get_time = 0.0

    def tearDown(self):
        signal.signal(signal.SIGALRM, self.old_handler)

