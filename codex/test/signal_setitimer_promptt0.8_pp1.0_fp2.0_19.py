import signal
# Test signal.setitimer.

from test.test_support import verify, verbose, run_unittest

from signal import setitimer, ITIMER_REAL, ITIMER_VIRTUAL, ITIMER_PROF, \
                   ITIMER_REALPROF, SIGALRM

import time

VERIFY_INTERVAL=0.25

