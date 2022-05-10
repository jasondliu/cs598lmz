import signal
# Test signal.setitimer() by calling it with the following values:
#
# - ITIMER_REAL with zero, SIGALRM -> should not do anything (no timer).
#
# - ITIMER_REAL with non-zero, SIGALRM -> should raise an alarm after the
#   specified period (call handler passed to signal.signal()).
#
# - ITIMER_REAL/VIRTUAL with zero, SIGALRM/SIGVTALRM -> should raise an alarm
#   after the specified period (call handler passed to signal.signal()).
#
# - ITIMER_REAL/VIRTUAL with non-zero, SIGALRM/SIGVTALRM -> should raise an
#   alarm after the specified period (call handler passed to signal.signal()).
import os, sys, time
import test.support, unittest
if (lambda: 0)():
    # Skip this test on systems which cannot support setitimer(). It is a
    # Bad Idea to iterate over a bunch of values in your test when you're
    # not sure of their effect. See http://bugs.python.
