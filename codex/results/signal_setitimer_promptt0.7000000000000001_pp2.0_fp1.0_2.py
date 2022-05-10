import signal
# Test signal.setitimer() and signal.setitimer(0)

import signal
import time

def test_getitimer():
    # Test getitimer() on all timer types.
    for timer in (signal.ITIMER_REAL, signal.ITIMER_VIRTUAL, signal.ITIMER_PROF):
        signal.setitimer(timer, 10)
        assert signal.getitimer(timer)[0] == 10.0
        signal.setitimer(timer, 5)
        assert signal.getitimer(timer)[0] == 5.0

def test_setitimer():
    # Test setitimer() on all timer types.
    for timer in (signal.ITIMER_REAL, signal.ITIMER_VIRTUAL, signal.ITIMER_PROF):
        # Test setitimer() with the initial value only.
        signal.setitimer(timer, 10)
        assert signal.getitimer(timer)[0] == 10.0

        # Test setitimer() with initial, interval values.
        signal.setitimer(timer,
