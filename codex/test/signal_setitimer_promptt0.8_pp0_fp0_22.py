import signal
# Test signal.setitimer() by sending a SIGALRM to this process at specified
# intervals.

import os, sys
from test.test_support import verbose, TestSkipped, TestFailed

