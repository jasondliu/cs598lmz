import signal
# Test signal.setitimer, signal.getitimer, SIGALRM, itimer_gettime, itimer_settime,
# ITIMER_REAL, ITIMER_VIRTUAL, ITIMER_PROF, ITIMER_REALPROF

import os, time, sys
from test.support import run_unittest, requires_linux_version, requires_linux_version_or_later

def alarm_received(n, frame):
    print('SIGALRM received')
    raise SystemExit

def itimer_virtual_received(n, frame):
    print('SIGVTALRM received')
    raise SystemExit

class ItimerTest(unittest.TestCase):

    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, signal.SIG_DFL)
        self.old_itimer_virtual = signal.signal(signal.SIGVTALRM,
                                                signal.SIG_DFL)

    def tearDown(self):
        signal.signal(signal.SIGAL
