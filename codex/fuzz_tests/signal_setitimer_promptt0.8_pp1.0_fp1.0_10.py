import signal
# Test signal.setitimer() and signal.getitimer()
# requirements: have /bin/sleep

import sys, os
from test.support import reap_children, run_unittest
from test.support import import_module
signal = import_module('signal')

# /bin/sleep does not exist on all platforms, and even when it does,
# it may be a wrapper that calls the real sleep in a different process.
# So we use a sleep written in Python.
# import time
# def mysleep(sec):
#     time.sleep(sec)

def mysleep(sec):
    # time.sleep(sec)
    # os.system("sleep %d" % sec)
    os.spawnv(os.P_WAIT, sys.executable, [sys.executable, '-c',
                                          'import time; time.sleep(%d)'%sec])

class AlarmTest(unittest.TestCase):
    def setUp(self):
        self.old_alarm = signal.signal(signal.SIGALRM, self.alarm_handler)
