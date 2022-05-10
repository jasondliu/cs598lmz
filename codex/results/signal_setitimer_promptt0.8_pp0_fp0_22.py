import signal
# Test signal.setitimer() by sending a SIGALRM to this process at specified
# intervals.

import os, sys
from test.test_support import verbose, TestSkipped, TestFailed

if sys.platform[:3] == 'win':
    raise TestSkipped, "setitimer is not implemented on Windows"

if not hasattr(signal, "setitimer"):
    raise TestSkipped, "no setitimer() in signal module"

interval = 0.1     # Time between timer interrupts

def handler(signum, frame):
    """Interrupt handler."""
    # Every third (double) SIGALRM, raise an exception to cause
    # setitimer() to calculate the next timer interval incorrectly.
    # For more info, see SF bug #876887.
    if signum == signal.SIGALRM and frame.f_back.f_lineno == 27:
        raise SystemError   # this is not caught
    if signum == signal.SIGALRM and frame.f_back.f_lineno == 31:
        raise AttributeError # this is caught
