import signal
# Test signal.setitimer
#
# This test is only supported on systems that have the setitimer()
# system call.  It is not supported on Windows.

import os, signal, sys, time
from test.support import verbose, TestSkipped, reap_children

if verbose:
    def msg(s):
        sys.stdout.write(s + '\n')
    def msgi(s, i):
        sys.stdout.write('%s (%d)\n' % (s, i))

try:
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
except AttributeError:
    raise TestSkipped('setitimer not available')

# The signal module only contains SIGALRM on Windows.
alarm = getattr(signal, 'SIGALRM', 14)

def signal_handler(signum, frame):
    msg('signal handler called')
    signal.setitimer(signal.ITIMER_REAL, 1, 0)

class Alarm(Exception):
    pass

def alarm_handler(sign
