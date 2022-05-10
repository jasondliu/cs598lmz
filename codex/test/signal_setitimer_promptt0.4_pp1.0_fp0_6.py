import signal
# Test signal.setitimer()
#
# This test is not run by default.  To run it, do:
#
#   python -Wd test_signal.py test_setitimer
#
# We can't use the standard test framework for this test, since we need
# to call setitimer() from a signal handler.

import sys
import time

from test.support import verbose, import_module

if verbose:
    def report(msg):
        print(msg)
else:
    def report(msg):
        pass

# The following is a list of (signal number, signal name) pairs.
# If a signal is not supported on a particular platform, it is
# not included in the list.

signals = []

if hasattr(signal, 'SIGALRM'):
    signals.append((signal.SIGALRM, 'SIGALRM'))

if hasattr(signal, 'SIGVTALRM'):
    signals.append((signal.SIGVTALRM, 'SIGVTALRM'))

