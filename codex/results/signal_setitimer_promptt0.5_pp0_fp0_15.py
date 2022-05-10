import signal
# Test signal.setitimer (issue #12984)
import time
import unittest

from test import support

# Skip this test if the platform doesn't support itimer.
if not hasattr(signal, 'setitimer'):
    raise unittest.SkipTest('platform does not support setitimer')

# Skip this test if the platform doesn't support SIGALRM.
if signal.getsignal(signal.SIGALRM) == signal.SIG_IGN:
    raise unittest.SkipTest('platform does not support SIGALRM')

# Skip this test if the platform doesn't support SIGUSR1.
if signal.getsignal(signal.SIGUSR1) == signal.SIG_IGN:
    raise unittest.SkipTest('platform does not support SIGUSR1')

# Skip this test if the platform doesn't support SIGUSR2.
if signal.getsignal(signal.SIGUSR2) == signal.SIG_IGN:
    raise unittest.SkipTest('platform does not support SIGUSR2')

# Skip this test if
