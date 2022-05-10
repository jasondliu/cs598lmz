import signal
# Test signal.setitimer
#
# This test is not very good because it only tests that setitimer()
# returns 0.  It does not test that the timer actually works.

import signal

signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
