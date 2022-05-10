import signal
# Test signal.setitimer(), signal.getitimer().
# The BSD version of signal.setitimer() doesn't seem to work, so we
# don't test it.
import os
import time

signal.signal(signal.SIGALRM, lambda sig, frame: None)

if os.name == 'posix':
    # POSIX
    signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)
    time.sleep(0.5)
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
    t = signal.getitimer(signal.ITIMER_REAL)
    signal.setitimer(signal.ITIMER_REAL, 0, 0)
    assert t[0] < 0.2
    assert t[1] == 0.1
    signal.setitimer(signal.ITIMER_VIRTUAL, 0.1, 0.1)
    time.sleep(0.5)
